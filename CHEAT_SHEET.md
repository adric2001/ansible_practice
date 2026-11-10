# Ansible Quick Reference Cheat Sheet

A comprehensive, production-oriented reference for Ansible syntax, CLI commands, patterns, and best practices.

---

## 1. Essential CLI Commands

### Ad-Hoc Command Syntax
```bash
ansible <host-pattern> -i <inventory> -m <module> -a "<arguments>" [options]
```

### Common Ad-Hoc Operations
```bash
# Ping hosts
ansible all -i lab/inventory.ini -m ansible.builtin.ping

# Execute shell command
ansible webservers -i lab/inventory.ini -m ansible.builtin.command -a "uptime"

# Gather specific facts
ansible all -i lab/inventory.ini -m ansible.builtin.setup -a "filter=ansible_distribution*"

# Install package (with become)
ansible webservers -i lab/inventory.ini -b -m ansible.builtin.package -a "name=nginx state=present"

# Restart service
ansible webservers -i lab/inventory.ini -b -m ansible.builtin.service -a "name=nginx state=restarted"

# Copy file with permissions
ansible webservers -i lab/inventory.ini -m ansible.builtin.copy -a "src=file.txt dest=/tmp/file.txt mode=0644"
```

### Playbook Execution Flags
```bash
# Check syntax
ansible-playbook --syntax-check playbook.yml

# Dry run (Check mode & Diff)
ansible-playbook playbook.yml --check --diff

# Limit execution to specific host/group
ansible-playbook playbook.yml --limit web01

# Step-by-step interactive execution
ansible-playbook playbook.yml --step

# Start execution at specific task
ansible-playbook playbook.yml --start-at-task="Deploy application"

# Pass extra variables (highest precedence)
ansible-playbook playbook.yml -e "app_version=2.1.0 env=prod"

# List all tasks / hosts in playbook
ansible-playbook playbook.yml --list-tasks
ansible-playbook playbook.yml --list-hosts
```

---

## 2. Ansible Vault Commands

```bash
# Create new encrypted file
ansible-vault create secret.yml

# Encrypt existing file
ansible-vault encrypt credentials.yml --vault-password-file .vault_password

# View encrypted file
ansible-vault view secret.yml --vault-password-file .vault_password

# Edit encrypted file in place
ansible-vault edit secret.yml --vault-password-file .vault_password

# Decrypt file permanently
ansible-vault decrypt secret.yml --vault-password-file .vault_password

# Change vault password (rekey)
ansible-vault rekey secret.yml --vault-password-file .vault_password

# Encrypt single variable string
ansible-vault encrypt_string 'MySecretPassword' --name 'db_password'
```

---

## 3. Variable Precedence (Lowest to Highest)

1. `roles/*/defaults/main.yml`
2. Inventory group_vars / `all`
3. Inventory group_vars / specific group
4. Inventory host_vars / `all`
5. Inventory host_vars / specific host
6. Playbook `group_vars/all`
7. Playbook `group_vars/group_name`
8. Playbook `host_vars/hostname`
9. Host facts / cached facts
10. Playbook `vars_prompt`
11. Playbook `vars_files`
12. Playbook `vars:`
13. `set_fact` / registered vars
14. Role `vars/main.yml`
15. Block `vars:`
16. Task `vars:`
17. Extra vars `-e "var=value"` (**Highest precedence - overrides everything**)

---

## 4. Jinja2 Filters & Manipulation

```jinja2
{# Default fallback #}
{{ app_port | default(8080) }}

{# Case formatting #}
{{ server_env | upper }}
{{ server_name | lower }}

{# Type conversion #}
{{ is_enabled | bool }}
{{ port_number | int }}

{# List processing #}
{{ host_list | unique | sort | list }}
{{ users | map(attribute='name') | join(', ') }}

{# JSON & YAML formatting #}
{{ my_dict | to_nice_json }}
{{ my_dict | to_nice_yaml(indent=2) }}

{# Base64 encoding/decoding #}
{{ secret_val | b64encode }}
{{ cert_b64 | b64decode }}

{# Regular expressions #}
{{ raw_version | regex_replace('^v', '') }}
```

---

## 5. Loops & Control Structures

```yaml
# Simple list loop
- name: Install packages
  ansible.builtin.package:
    name: "{{ item }}"
    state: present
  loop:
    - curl
    - git
    - htop

# Complex dict loop with label
- name: Create users
  ansible.builtin.user:
    name: "{{ item.name }}"
    shell: "{{ item.shell | default('/bin/bash') }}"
  loop: "{{ user_list }}"
  loop_control:
    label: "{{ item.name }}"
    index_var: idx

# Polling retry loop
- name: Wait for API service to be healthy
  ansible.builtin.uri:
    url: "http://localhost:8080/health"
    status_code: 200
  register: result
  until: result.status == 200
  retries: 10
  delay: 3
```

---

## 6. Block, Rescue, & Always Pattern

```yaml
- name: Transactional Block with Rollback
  block:
    - name: Primary operation
      ansible.builtin.command: /opt/app/migrate_db.sh
  rescue:
    - name: Run only if block tasks fail
      ansible.builtin.command: /opt/app/rollback_db.sh
  always:
    - name: Guaranteed cleanup (runs regardless of outcome)
      ansible.builtin.file:
        path: /tmp/migration.lock
        state: absent
```
