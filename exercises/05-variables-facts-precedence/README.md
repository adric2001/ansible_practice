# Exercise 05: Variables, Facts, & Precedence

## 🎯 Objective
Master the Ansible variable hierarchy, understand how facts are gathered and filtered, inspect magic variables (`hostvars`, `groups`), and utilize `set_fact` and registered variables.

## 📖 Key Concepts

### 1. Variable Precedence (Summary)
Ansible evaluates variables with an explicit order of precedence (lowest to highest):
1. Role defaults (`roles/x/defaults/main.yml`)
2. Inventory group_vars
3. Inventory host_vars
4. Playbook `group_vars/` and `host_vars/`
5. Playbook `vars:` and `vars_files:`
6. Task `vars:`
7. Dynamic facts created via `set_fact`
8. Extra variables passed via CLI (`-e key=value`) - **Highest priority!**

### 2. Magic Variables
- `inventory_hostname`: Name of the current host as defined in inventory.
- `groups`: Dictionary of all groups and the hosts belonging to them.
- `group_names`: List of groups the current host belongs to.
- `hostvars`: Allows host A to access facts and variables of host B! (e.g. `{{ hostvars['db01']['ansible_default_ipv4']['address'] }}`).

### 3. Gathering & Custom Facts
- Facts are stored in `ansible_facts` dictionary.
- Custom local facts can be placed on target nodes in `/etc/ansible/facts.d/<filename>.fact` (JSON, INI, or executable script returning JSON) and are exposed under `ansible_facts.ansible_local.<filename>`.

---

## 🏢 The Scenario
You need to build a system audit and reporting playbook that:
1. Defines default variables in `group_vars/` and overrides in `host_vars/`.
2. Inspects `ansible_facts` (IP address, architecture, total memory in GB).
3. Demonstrates variable precedence by defining a variable `deploy_environment` at group level, play level, and overriding it with `set_fact`.
4. Uses `hostvars` to discover and list all database server IPs from the perspective of a web node.
5. Saves a generated JSON summary to `/tmp/system_report.json`.

---

## 📝 Tasks
1. Inspect the provided `inventory.ini`, `group_vars/`, and `host_vars/`.
2. Complete `playbook.yml` to extract the system facts and evaluate variable precedence.
3. Verify the generated output.

---

## 🔍 Verification Commands

```bash
# Run against localhost
ansible-playbook -i inventory.ini -c local playbook.yml

# Test extra vars override (highest precedence)
ansible-playbook -i inventory.ini -c local playbook.yml -e "app_log_level=DEBUG"
```

