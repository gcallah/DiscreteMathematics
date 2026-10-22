#!/usr/bin/env bash
# Stop this workspace's dev server and release its port.
set -uo pipefail
cd "$(dirname "$0")/.."
. .superset/env.sh

PORT="$($PORTS lookup "$WORKSPACE_KEY" 2>/dev/null || true)"
if [ -n "$PORT" ]; then
  for pid in $(lsof -ti "tcp:$PORT" -sTCP:LISTEN 2>/dev/null); do
    cwd="$(lsof -a -p "$pid" -d cwd -Fn 2>/dev/null | sed -n 's/^n//p')"
    [ "$cwd" = "$(pwd -P)" ] && kill "$pid" 2>/dev/null
  done
fi
$PORTS release "$WORKSPACE_KEY" || true
exit 0
