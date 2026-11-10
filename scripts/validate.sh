#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

export ANSIBLE_LOCAL_TEMP="${ANSIBLE_LOCAL_TEMP:-/tmp/ansible-local}"
export ANSIBLE_REMOTE_TEMP="${ANSIBLE_REMOTE_TEMP:-/tmp/ansible-remote}"
mkdir -p "${ANSIBLE_LOCAL_TEMP}" "${ANSIBLE_REMOTE_TEMP}"

# Discover python binary with PyYAML
PYTHON_BIN=""
for candidate in \
    "/opt/homebrew/Cellar/ansible/14.4.0/libexec/bin/python" \
    "/opt/homebrew/bin/python3" \
    "$(which python3 2>/dev/null)"; do
    if [ -x "${candidate}" ] && "${candidate}" -c "import yaml" >/dev/null 2>&1; then
        PYTHON_BIN="${candidate}"
        break
    fi
done

if [ -z "${PYTHON_BIN}" ]; then
    PYTHON_BIN="python3"
fi

"${PYTHON_BIN}" "${SCRIPT_DIR}/test_runner.py" "$@"
