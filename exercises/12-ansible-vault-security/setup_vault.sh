#!/usr/bin/env bash
# Script to prepare Vault secrets for Exercise 12
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${DIR}"

echo ">> 1. Creating demo vault password file (.vault_password)..."
echo "practice_vault_pass_123" > .vault_password
chmod 600 .vault_password

echo ">> 2. Generating unencrypted secret template..."
cat << 'EOF' > vault_secret.yml
---
payment_gateway_api_key: "sk_live_998877665544332211"
database_master_password: "SuperSecretVaultPassword!#2026"
jwt_signing_key: "base64:7a9fbc102384a9e8d7c6b5a4"
EOF

echo ">> 3. Encrypting vault_secret.yml using ansible-vault..."
export ANSIBLE_LOCAL_TEMP="${ANSIBLE_LOCAL_TEMP:-/tmp/ansible-local}"
export ANSIBLE_REMOTE_TEMP="${ANSIBLE_REMOTE_TEMP:-/tmp/ansible-remote}"
ansible-vault encrypt vault_secret.yml --vault-password-file .vault_password

echo ">> Vault encrypted successfully!"
echo "Inspect with: ansible-vault view vault_secret.yml --vault-password-file .vault_password"

