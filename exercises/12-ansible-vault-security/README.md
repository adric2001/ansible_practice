# Exercise 12: Ansible Vault & Secrets Management

## 🎯 Objective
Learn how to protect sensitive credentials (passwords, tokens, private keys) at rest using Ansible Vault, inline string encryption, vault password files, and multi-vault IDs.

## 📖 Key Concepts

### 1. Ansible Vault CLI Commands
| Action | Command |
| :--- | :--- |
| Create new encrypted file | `ansible-vault create secret.yml` |
| Encrypt existing plain file | `ansible-vault encrypt credentials.yml` |
| View encrypted contents | `ansible-vault view credentials.yml` |
| Edit encrypted file in place | `ansible-vault edit credentials.yml` |
| Decrypt permanently | `ansible-vault decrypt credentials.yml` |
| Change vault password | `ansible-vault rekey credentials.yml` |
| Encrypt single variable string | `ansible-vault encrypt_string 'MySecret' --name 'db_password'` |

### 2. Passing Vault Passwords to Playbooks
- Interactive prompt: `--ask-vault-pass`
- Password file: `--vault-password-file ~/.vault_pass`
- Environment variable: `export ANSIBLE_VAULT_PASSWORD_FILE=/path/to/pass.txt`
- Vault IDs (for multiple environments): `--vault-id dev@pass_dev.txt --vault-id prod@pass_prod.txt`

### 3. Best Practice: Layered Variables
Instead of encrypting an entire 200-line config file, encrypt only the secret strings or isolate secrets into a separate `vault.yml` paired with an unencrypted `vars.yml`:
```text
group_vars/production/
├── vars.yml   # Unencrypted configuration (ports, domain names, log levels)
└── vault.yml  # Encrypted secrets (database passwords, API tokens, certs)
```

---

## 🏢 The Scenario
You are securing API gateway tokens and database passwords for a payment service:
1. Create a password file `.vault_password` containing a demo vault password `practice_vault_pass_123`.
2. Encrypt `vault_secret.yml` using `ansible-vault encrypt`.
3. Use `ansible-vault encrypt_string` to create an inline encrypted string.
4. Run a playbook that decrypts the secrets in memory and renders a secure configuration file at `/tmp/ansible_vault_lab/payment_service.env` without exposing the plain password in Git!

---

## 📝 Tasks
1. Follow the steps in `setup_vault.sh` to generate the encrypted secret files.
2. Complete `playbook.yml`.

---

## 🔍 Verification Commands

```bash
# Execute playbook with vault password file
ansible-playbook -i "localhost," -c local --vault-password-file .vault_password playbook.yml

# Verify the rendered file contains the decrypted secret
cat /tmp/ansible_vault_lab/payment_service.env
```
