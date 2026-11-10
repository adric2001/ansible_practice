#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== [Ansible Practice Lab Teardown] ==="
cd "${SCRIPT_DIR}"
docker compose down -v --remove-orphans
echo ">> Lab containers stopped and cleaned up."

