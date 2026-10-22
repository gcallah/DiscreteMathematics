#!/usr/bin/env python3
"""Per-workspace port registry shared by all Superset workspaces.

Usage: ports.py reserve|get|lookup|release <workspace-key>
Allocations live in ~/.superset/port-allocations.json, guarded by an fcntl lock.
"""
import fcntl
import json
import os
import socket
import sys

RANGE = range(8100, 8200)
REGISTRY = os.path.expanduser("~/.superset/port-allocations.json")
SECTION = "DiscreteMathematics"


def is_free(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind(("127.0.0.1", port))
            return True
        except OSError:
            return False


def main():
    cmd, key = sys.argv[1], sys.argv[2]
    os.makedirs(os.path.dirname(REGISTRY), exist_ok=True)
    with open(REGISTRY + ".lock", "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        try:
            with open(REGISTRY) as f:
                data = json.load(f)
        except (FileNotFoundError, ValueError):
            data = {}
        mine = data.setdefault(SECTION, {})
        taken = {p for s in data.values() for p in s.values()}
        port = mine.get(key)

        if cmd == "lookup":
            # Read-only: report the reserved port without reallocating.
            if port is not None:
                print(port)
            return
        if cmd == "release":
            mine.pop(key, None)
        elif cmd in ("reserve", "get"):
            # Keep the existing port unless something outside the registry grabbed it.
            if port is None or (cmd == "get" and not is_free(port)):
                taken.discard(port)
                port = next((p for p in RANGE if p not in taken and is_free(p)), None)
                if port is None:
                    sys.exit("no free port in %d-%d" % (RANGE.start, RANGE.stop - 1))
                mine[key] = port
            print(port)
        else:
            sys.exit("unknown command: " + cmd)

        tmp = REGISTRY + ".tmp"
        with open(tmp, "w") as f:
            json.dump(data, f, indent=2, sort_keys=True)
        os.replace(tmp, REGISTRY)


if __name__ == "__main__":
    main()
