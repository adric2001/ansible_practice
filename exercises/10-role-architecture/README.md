# Exercise 10: Reusable Role Architecture

## 🎯 Objective
Learn how to structure, develop, and invoke modular, reusable Ansible roles following industry best practices.

## 📖 Key Concepts

### 1. Standard Role Directory Structure
An Ansible role adheres to a standardized directory layout:
```text
roles/common_security/
├── defaults/
│   └── main.yml        # Lowest precedence variables, meant to be overridden by consumers
├── vars/
│   └── main.yml        # High precedence variables, internal role constants
├── tasks/
│   └── main.yml        # Core task execution entrypoint
├── handlers/
│   └── main.yml        # Handlers triggered by role tasks
├── templates/
│   └── audit.conf.j2   # Jinja2 templates deployed by the role
├── files/
│   └── banner.txt      # Static files copied by the role
└── meta/
    └── main.yml        # Metadata, author, supported platforms, role dependencies
```

### 2. Invoking Roles
- Classic: `roles: [ common_security ]`
- Dynamic: `ansible.builtin.include_role` (evaluated at runtime, allows dynamic role names/loops).
- Static: `ansible.builtin.import_role` (parsed at playbook compilation time).

---

## 🏢 The Scenario
You need to construct a reusable `common_security` role:
1. `defaults/main.yml`: default port, banner path, security audit level (`STANDARD`).
2. `tasks/main.yml`:
   - Deploys static security notice from `files/`.
   - Renders security audit configuration from `templates/`.
   - Manages an administrative group with configurable GID.
3. Playbook invocation: invoke the role twice: once with default settings, and once with customized overrides (`audit_level: STRICT`).

---

## 📝 Tasks
1. Complete the role directory structure under `roles/common_security/`.
2. Complete `playbook.yml`.

---

## 🔍 Verification Commands

```bash
# Execute against localhost
ansible-playbook -i "localhost," -c local playbook.yml
```
