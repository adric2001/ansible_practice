# Exercise 01: Inventory Fundamentals (INI & YAML)

## 🎯 Objective
Learn how to define, organize, and query Ansible static inventories using both INI and YAML syntax, including host variables, group variables, and nested (child) groups.

## 📖 Key Concepts
- **Inventory Format**: Ansible supports both INI (`.ini`) and YAML (`.yml`/`.yaml`) formats.
- **Host Variables**: Variables specific to a single host (e.g., `ansible_host`, `ansible_port`, `custom_ip`).
- **Group Variables**: Variables shared across all members of a group (e.g., `http_port: 8080`).
- **Nested Groups (`children`)**: Groups that contain other groups (e.g., `production` containing `web_prod` and `db_prod`).
- **Special Connection Variables**:
  - `ansible_host`: The actual IP address or FQDN to connect to.
  - `ansible_port`: Custom SSH port (default: 22).
  - `ansible_user`: The user Ansible uses to SSH into the host.
  - `ansible_connection`: Connection plugin (`ssh`, `local`, `docker`, etc.).

---

## 🏢 The Scenario
You are the Infrastructure Engineer at **Apex Cloud Solutions**. You need to design an inventory reflecting their hybrid infrastructure:

1. **Hosts & Tiers**:
   - Web Servers:
     - `web-prod-01`: IP `192.168.10.11`, SSH port `22`, user `deploy`
     - `web-prod-02`: IP `192.168.10.12`, SSH port `22`, user `deploy`
     - `web-stage-01`: IP `192.168.20.11`, SSH port `2222`, user `stageuser`
   - Database Servers:
     - `db-prod-primary`: IP `192.168.10.50`, SSH port `22`, role `primary`
     - `db-prod-replica`: IP `192.168.10.51`, SSH port `22`, role `replica`
     - `db-stage-01`: IP `192.168.20.50`, SSH port `22`, role `standalone`
   - Management / Bastion:
     - `bastion-01`: IP `10.0.0.1`, SSH port `2200`
   - Local Control Machine:
     - `localhost`: uses `ansible_connection=local`

2. **Group Hierarchy**:
   - `web`: contains all web servers (`web-prod-01`, `web-prod-02`, `web-stage-01`)
   - `databases`: contains all database servers
   - `production`: contains `web-prod-01`, `web-prod-02`, `db-prod-primary`, `db-prod-replica`
   - `staging`: contains `web-stage-01`, `db-stage-01`
   - `all`: parent of all groups

3. **Variables**:
   - For group `production`: `env_type: production`, `monitoring_enabled: true`
   - For group `staging`: `env_type: staging`, `monitoring_enabled: false`
   - For group `web`: `http_port: 80`
   - For group `all`: `ntp_server: pool.ntp.org`

---

## 📝 Tasks

1. Review `starter_inventory.ini` and complete the missing hosts, groups, and variables according to the requirements.
2. Convert the completed INI inventory into an equivalent YAML format in `starter_inventory.yml`.
3. Use `ansible-inventory` command to inspect, graph, and validate your inventory.

---

## 🔍 Verification Commands

Test your inventory using Ansible's built-in inventory inspection tool:

```bash
# 1. View the parsed inventory graph
ansible-inventory -i starter_inventory.ini --graph

# 2. View all hosts and their resolved variables in JSON
ansible-inventory -i starter_inventory.ini --list

# 3. Query resolved variables for a single host
ansible-inventory -i starter_inventory.ini --host web-prod-01

# 4. Check YAML inventory syntax
ansible-inventory -i starter_inventory.yml --graph
```

---

## 💡 Hints
- In INI, child groups are declared with the `[group_name:children]` header.
- Group variables in INI are declared with the `[group_name:vars]` header.
- In YAML, child groups go under `children:`, and group variables go under `vars:`.
- Check the `solution/` directory when you're done or if you get stuck.

