# Shared variables for the Superset lifecycle scripts (sourced, not executed).
WORKTREE="$(git rev-parse --show-toplevel)"
if [ -z "${SUPERSET_ROOT_PATH:-}" ]; then
  SUPERSET_ROOT_PATH="$(dirname "$(git rev-parse --path-format=absolute --git-common-dir)")"
fi
WORKSPACE_KEY="${SUPERSET_WORKSPACE_NAME:-$WORKTREE}"
PORTS="python3 $WORKTREE/.superset/ports.py"
