#!/usr/bin/env sh

#!/usr/bin/env bash

# Usage:
#   ./upload.sh $USER $HOST $LOCAL_DIRECTORY $REMOTE_PATH
#
# Defaults:
#   HOST = "cunix.columbia.edu"
#   LOCAL_DIRECTORY = "./dist"
#   REMOTE_PATH = "$HOME/public_html/"
#
# Example using defaults:
#   ./upload.sh abc123
#
# Example overriding defaults:
#   ./upload.sh abc123 cunix.columbia.edu ./dist $HOME/public_html/

set -euo pipefail

DEFAULT_HOST="cunix.columbia.edu"
DEFAULT_LOCAL_DIR="./dist"
DEFAULT_REMOTE_PATH="~/public_html/"

if [[ $# -lt 1 || $# -gt 4 ]]; then
  echo "Usage: $0 \$USER \$HOST \$LOCAL_DIRECTORY \$REMOTE_PATH" >&2
  exit 1
fi

user="$1"
host="${2:-$DEFAULT_HOST}"
local_dir="${3:-$DEFAULT_LOCAL_DIR}"
remote_path="${4:-$DEFAULT_REMOTE_PATH}"

if [[ ! -d "$local_dir" ]]; then
  echo "Error: local directory does not exist: $local_dir" >&2
  exit 1
fi

scp -O -r "$local_dir"/* "$user@$host:$remote_path"

echo "Files uploaded successfully."
