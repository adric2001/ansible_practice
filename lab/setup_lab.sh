#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SSH_DIR="${SCRIPT_DIR}/ssh_keys"

echo "=== [Ansible Practice Lab Setup] ==="

# 1. Generate SSH key pair if not exists
mkdir -p "${SSH_DIR}"
if [ ! -f "${SSH_DIR}/id_rsa" ]; then
    echo ">> Generating dedicated SSH keypair in ${SSH_DIR}..."
    ssh-keygen -t rsa -b 2048 -f "${SSH_DIR}/id_rsa" -N "" -C "ansible-practice-lab"
    chmod 600 "${SSH_DIR}/id_rsa"
    chmod 644 "${SSH_DIR}/id_rsa.pub"
fi

# 2. Build and start containers
echo ">> Spinning up multi-node Docker lab (web01, web02, db01)..."
cd "${SCRIPT_DIR}"
docker compose up -d --build

echo ""
echo ">> Waiting for containers and SSH services to initialize..."
sleep 3

echo ""
echo "=== Lab Ready! ==="
echo "Nodes available:"
echo " - web01 (Port 2221)"
echo " - web02 (Port 2222)"
echo " - db01  (Port 2223)"
echo ""
echo "Test connectivity with:"
echo " ansible -i lab/inventory.ini all -m ping"
