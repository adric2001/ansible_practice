# Exercise 04: Package & Service Management Across Distributions

## 🎯 Objective
Learn how to manage packages and system services across different Linux distributions in an idempotent, platform-agnostic manner.

## 📖 Key Concepts
- **Abstract Package Module**: `ansible.builtin.package` acts as a generic wrapper around OS package managers (`apt`, `dnf`, `yum`, `apk`, `brew`).
- **OS-Specific Modules**:
  - `ansible.builtin.apt`: Debian/Ubuntu (supports `update_cache`, `cache_valid_time`).
  - `ansible.builtin.dnf`: RHEL/CentOS/Fedora/Rocky.
- **Service Management**:
  - `ansible.builtin.service`: Generic init/systemd service controller.
  - `ansible.builtin.systemd`: Explicit systemd module (supports `daemon_reload`, `masked`, `scope`).
- **Inspecting Services**:
  - `ansible.builtin.service_facts`: Gathers all system service states into `ansible_facts.services`.

---

## 🏢 The Scenario
You need to write a cross-platform playbook that:
1. Detects the OS family (`ansible_facts['os_family']`).
2. Defines package name mappings:
   - For `Debian`: Apache is `apache2`, tools are `['curl', 'htop', 'git']`.
   - For `RedHat`: Apache is `httpd`, tools are `['curl', 'htop', 'git']`.
   - For `Darwin` (macOS): uses `git`, `curl`.
3. Ensures all utility packages are installed and up to date (`state: present`).
4. Uses `ansible.builtin.service_facts` to inspect existing services.
5. Manages service state and ensures auto-start on boot (`enabled: true`, `state: started`).

---

## 📝 Tasks
Open `playbook.yml` and implement the tasks according to the specification.

---

## 🔍 Verification Commands

Test your playbook:
```bash
# Test against Docker lab nodes:
ansible-playbook -i lab/inventory.ini --limit webservers playbook.yml

# Or check syntax:
ansible-playbook --syntax-check playbook.yml
```
