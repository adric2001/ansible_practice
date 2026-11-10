# Exercise 02: Ad-Hoc Operations & CLI Mastery

## 🎯 Objective
Master the Ansible CLI ad-hoc command syntax (`ansible`) to execute rapid one-off administration tasks without writing a full playbook.

## 📖 Key Concepts
Ansible ad-hoc commands are ideal for quick queries, emergency reboots, inspecting node states, and fast verification:

```bash
ansible <host-pattern> -i <inventory> -m <module> -a "<module-arguments>" [options]
```

Key CLI Flags:
| Flag | Description | Example |
| :--- | :--- | :--- |
| `-m` | Module name (default is `command`) | `-m ping` |
| `-a` | Arguments passed to the module | `-a "free -m"` |
| `-i` | Inventory path or inline comma-separated host list | `-i lab/inventory.ini` |
| `-b` | Become (privilege escalation, sudo) | `-b` |
| `-o` | Condense output to a single line per host | `-o` |
| `-f` | Number of parallel forks (concurrency) | `-f 10` |
| `-e` | Pass extra variables | `-e "app_version=2.0"` |
| `-C` | Check mode (dry-run, no changes made) | `-C` |

---

## 🏢 The Scenario
You are on-call during a high-traffic release. You need to execute 8 critical operational tasks across your fleet using **only** ad-hoc commands:

1. **Fleet Health Check**: Ping all hosts in the inventory to verify connectivity.
2. **Fact Filtering**: Query only the OS distribution and memory facts of all nodes using `setup` module with `filter`.
3. **Emergency Disk Audit**: Run a shell command to view disk space (`df -h /`) on all web servers in one-line output format.
4. **Distribute Security Alert Notice**: Copy a local file to `/tmp/security_alert.txt` on all nodes with permissions `0644`.
5. **Create Audit User**: Ensure a user named `auditor` with UID `1500` exists on all nodes with sudo privileges disabled.
6. **Package Verification**: Use check mode (`-C`) to check if `curl` is present on the hosts.
7. **Service Status Check**: Check if the `ssh` / `sshd` service is running without altering it.
8. **File Permission Hardening**: Change permissions of `/tmp/security_alert.txt` to `0600` and owner to current user.

---

## 📝 Tasks & Starter File
Open `challenges.sh`. You will find 8 empty shell functions corresponding to the 8 scenarios. Complete each command using `ansible`.

---

## 🔍 Verification Commands

Run your challenge script to test:
```bash
# Test against localhost:
./challenges.sh localhost

# Or test against Docker lab:
./challenges.sh lab
```

---

## 💡 Hints
- Default module if `-m` is omitted is `ansible.builtin.command`.
- For `ansible.builtin.setup`, use the `filter` argument: `-a "filter=ansible_distribution*"` or `-a "filter=ansible_memtotal_mb"`.
- For single-line output, append `-o`.
- Module names should use fully qualified collection names (FQCN) where possible: `ansible.builtin.ping`, `ansible.builtin.copy`, `ansible.builtin.user`, etc.
