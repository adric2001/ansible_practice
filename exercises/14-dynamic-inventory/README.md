# Exercise 14: Dynamic Inventory Development

## 🎯 Objective
Understand how Ansible discovers targets dynamically from cloud providers, hypervisors, and CMDBs by building a custom Python dynamic inventory script adhering to the Ansible Dynamic Inventory specification.

## 📖 Key Concepts

### 1. Dynamic Inventory Protocol
Ansible can execute any executable script or binary as an inventory if it responds to CLI flags with JSON:
1. When passed `--list`: Returns a JSON dictionary containing groups, child relationships, and host lists.
2. The `_meta` optimization:
   Instead of Ansible invoking the script once per host with `--host <hostname>`, the `--list` response can embed all host variables under top-level `_meta.hostvars`:
   ```json
   {
     "webservers": {
       "hosts": ["web-01", "web-02"],
       "vars": { "http_port": 80 }
     },
     "_meta": {
       "hostvars": {
         "web-01": { "ansible_host": "10.0.1.10", "environment": "prod" },
         "web-02": { "ansible_host": "10.0.1.11", "environment": "prod" }
       }
     }
   }
   ```

---

## 🏢 The Scenario
You need to connect Ansible to an external CMDB represented by `cmdb_data.json`.
1. Parse the JSON records of cloud instances.
2. Group them automatically by:
   - Environment (`prod`, `staging`)
   - Role (`web`, `database`, `cache`)
   - Region (`us-east`, `eu-west`)
3. Populate `_meta.hostvars` with their IP addresses, instance IDs, and tags.
4. Ensure the script is executable (`chmod +x dynamic_inventory.py`).
5. Query with `ansible-inventory` and run a playbook against the dynamic targets.

---

## 📝 Tasks
1. Complete `dynamic_inventory.py`.
2. Inspect with `ansible-inventory -i dynamic_inventory.py --graph`.
3. Run `playbook.yml`.

---

## 🔍 Verification Commands

```bash
# Test dynamic inventory output directly
./dynamic_inventory.py --list

# Test with ansible-inventory
ansible-inventory -i dynamic_inventory.py --graph
ansible-inventory -i dynamic_inventory.py --list

# Execute playbook against dynamic inventory
ansible-playbook -i dynamic_inventory.py playbook.yml
```
