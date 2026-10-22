#!/usr/bin/env bash
# Prepare a new Superset workspace. Safe to re-run.
set -euo pipefail
cd "$(dirname "$0")/.."
. .superset/env.sh

# utils/ holds the build scripts used by the makefiles; Algocynfas is linked from pages.
git submodule update --init utils Algocynfas

# Copy untracked env files from the main checkout (none exist today, so this is a no-op).
# Gradebooks/ and IaconeMaterials/ are deliberately NOT copied.
if [ "$(cd "$SUPERSET_ROOT_PATH" && pwd -P)" != "$(pwd -P)" ]; then
  for f in "$SUPERSET_ROOT_PATH"/.env "$SUPERSET_ROOT_PATH"/.env.*; do
    [ -f "$f" ] || continue
    [ -e "$(basename "$f")" ] || cp "$f" .
  done
fi

PORT="$($PORTS reserve "$WORKSPACE_KEY")"
echo "Workspace ready. Dev server port: $PORT"
