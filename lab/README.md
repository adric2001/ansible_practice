# Ansible Practice Lab Environments

This directory provides two flexible ways to run and practice Ansible:

## Option A: Localhost Mode (No Docker Required)
You can practice immediately on your local system without spinning up any containers.
All exercises support running against `localhost` with the local connection plugin:

```bash
ansible-playbook -i "localhost," -c local <playbook.yml>
```
Or simply use the `[local]` group inside `lab/inventory.ini`:
```bash
ansible-playbook -i lab/inventory.ini --limit local <playbook.yml>
```

---

## Option B: Multi-Node Docker Lab (Recommended for Realism)
Simulates a real-world multi-node cluster (`web01`, `web02`, `db01`) on your local machine using lightweight Docker containers with SSH and Python.

### Prerequisites
- Docker & Docker Compose installed.

### 1. Start the Lab
Run the setup script:
```bash
./lab/setup_lab.sh
```
This automatically:
1. Generates a secure SSH key pair under `lab/ssh_keys/`.
2. Builds the Ubuntu test node image.
3. Launches 3 containers on isolated ports (2221, 2222, 2223).

### 2. Verify Connectivity
Test Ansible connectivity across all nodes:
```bash
ansible -i lab/inventory.ini webservers -m ping
ansible -i lab/inventory.ini dbservers -m ping
ansible -i lab/inventory.ini all -m ping
```

### 3. Stop / Reset the Lab
When finished practicing:
```bash
./lab/teardown_lab.sh
```
