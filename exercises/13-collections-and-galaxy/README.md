# Exercise 13: Collections & Ansible Galaxy

## 🎯 Objective
Understand Ansible Collections architecture, declare dependencies via `collections/requirements.yml`, install collections with `ansible-galaxy`, and write modern playbooks using Fully Qualified Collection Names (FQCN).

## 📖 Key Concepts

### 1. What is an Ansible Collection?
A distribution format for Ansible content that can include:
- Playbooks
- Roles
- Modules
- Plugins (callback, filter, lookup, action, inventory, connection)

### 2. Fully Qualified Collection Names (FQCN)
Always reference modules by their complete namespace:
- ❌ Legacy: `copy:`, `sysctl:`, `ini_file:`
- ✅ Modern FQCN:
  - `ansible.builtin.copy`
  - `ansible.posix.sysctl`
  - `community.general.ini_file`
  - `community.crypto.openssl_privatekey`

### 3. Declaring Dependencies in `requirements.yml`
```yaml
---
collections:
  - name: ansible.posix
    version: ">=1.5.0"
  - name: community.general
    version: ">=8.0.0"
```

---

## 🏢 The Scenario
You need to:
1. Define a `requirements.yml` file listing `ansible.posix` and `community.general`.
2. Write a playbook utilizing modules from these collections with strict FQCN:
   - `community.general.ini_file` to manage an INI config file idempotently.
   - `ansible.builtin.assert` to test the resulting values.

---

## 📝 Tasks
1. Complete `collections/requirements.yml`.
2. Complete `playbook.yml`.

---

## 🔍 Verification Commands

```bash
# Check syntax
ansible-playbook --syntax-check playbook.yml

# Execute against localhost
ansible-playbook -i "localhost," -c local playbook.yml
```
