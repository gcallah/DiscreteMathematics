#!/usr/bin/env bash
# Serve the static site on this workspace's reserved port.
set -euo pipefail
cd "$(dirname "$0")/.."
. .superset/env.sh

PORT="$($PORTS get "$WORKSPACE_KEY")"
echo "Serving $WORKTREE at http://127.0.0.1:$PORT/"
exec python3 -m http.server "$PORT" --bind 127.0.0.1
