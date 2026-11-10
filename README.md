# 🚀 Ansible Practice Suite: Zero to Production

A comprehensive, hands-on curriculum of **20 progressive practice exercises** designed to take you from foundational Ansible concepts to advanced enterprise orchestration, custom module development, and production security compliance.

---

## 📚 Curriculum Roadmap

| # | Exercise | Difficulty | Key Focus Areas |
| :-: | :--- | :---: | :--- |
| **01** | [`01-inventory-fundamentals`](exercises/01-inventory-fundamentals) | 🟢 Beginner | INI & YAML formats, child groups, host/group variables |
| **02** | [`02-adhoc-operations`](exercises/02-adhoc-operations) | 🟢 Beginner | Ad-hoc CLI flags, quick diagnostics, facts filtering |
| **03** | [`03-playbook-basics-idempotency`](exercises/03-playbook-basics-idempotency) | 🟢 Beginner | Playbook structure, idempotency, file/directory management |
| **04** | [`04-package-and-service-management`](exercises/04-package-and-service-management) | 🟢 Beginner | Multi-distro package handling (`apt`, `dnf`), systemd services |
| **05** | [`05-variables-facts-precedence`](exercises/05-variables-facts-precedence) | 🟡 Intermediate | 22 precedence levels, `set_fact`, magic vars (`hostvars`) |
| **06** | [`06-loops-and-conditionals`](exercises/06-loops-and-conditionals) | 🟡 Intermediate | `loop`, `loop_control`, `when`, `failed_when`, `until` |
| **07** | [`07-handlers-and-notifications`](exercises/07-handlers-and-notifications) | 🟡 Intermediate | Handlers lifecycle, `listen` topics, `flush_handlers` |
| **08** | [`08-jinja2-templating`](exercises/08-jinja2-templating) | 🟡 Intermediate | Filters, whitespace trimming, loop control in templates |
| **09** | [`09-error-handling-and-blocks`](exercises/09-error-handling-and-blocks) | 🟡 Intermediate | `block`, `rescue`, `always`, automated rollback strategies |
| **10** | [`10-role-architecture`](exercises/10-role-architecture) | 🟡 Intermediate | Standard role structure, defaults vs vars, meta dependencies |
| **11** | [`11-multitier-application-stack`](exercises/11-multitier-application-stack) | 🔴 Advanced | Multi-play orchestration, 3-tier topology (DB, App, LB) |
| **12** | [`12-ansible-vault-security`](exercises/12-ansible-vault-security) | 🔴 Advanced | Encrypting secrets, vault IDs, password files, inline strings |
| **13** | [`13-collections-and-galaxy`](exercises/13-collections-and-galaxy) | 🔴 Advanced | Modern FQCN standard, `requirements.yml`, Ansible Galaxy |
| **14** | [`14-dynamic-inventory`](exercises/14-dynamic-inventory) | 🔴 Advanced | Custom Python dynamic inventory script, CMDB integration |
| **15** | [`15-strategies-delegation-rolling-updates`](exercises/15-strategies-delegation-rolling-updates) | 🔴 Advanced | Canary batches (`serial`), `max_fail_percentage`, `delegate_to` |
| **16** | [`16-custom-modules`](exercises/16-custom-modules) | 🔴 Advanced | Custom Python module (`AnsibleModule`), check mode support |
| **17** | [`17-custom-filter-plugins`](exercises/17-custom-filter-plugins) | 🔴 Advanced | Custom Jinja2 filter plugins in Python, data transformation |
| **18** | [`18-custom-callback-plugins`](exercises/18-custom-callback-plugins) | 🔴 Advanced | Event interceptors, structured JSON audit logging |
| **19** | [`19-testing-and-linting`](exercises/19-testing-and-linting) | 🔴 Advanced | Refactoring anti-patterns, Molecule style `assert` tests |
| **20** | [`20-security-hardening-and-compliance`](exercises/20-security-hardening-and-compliance) | 🔴 Advanced | CIS benchmark baseline, SSH & kernel sysctl hardening |
| **21** | [`21-async-and-polling`](exercises/21-async-and-polling) | 🔴 Advanced | Asynchronous execution (`async`, `poll`), `async_status` monitoring |

---

## 🛠️ Environment Setup & Quickstart

You have two convenient ways to practice:

### Option 1: Localhost Mode (Instant, No Docker Needed)
Every exercise in this repository is configured so you can immediately execute it on your local workstation without spinning up external servers:
```bash
ansible-playbook -i "localhost," -c local <playbook.yml>
```

### Option 2: Docker Multi-Node Cluster (Realistic Lab)
If you want to practice managing multiple remote Linux nodes over SSH:
```bash
# 1. Start the lab (builds & starts 3 SSH-enabled Ubuntu nodes: web01, web02, db01)
./lab/setup_lab.sh

# 2. Test connectivity across all nodes
ansible all -i lab/inventory.ini -m ping

# 3. When finished practicing, tear down the lab
./lab/teardown_lab.sh
```

---

## 🎯 How to Practice Each Exercise

Each exercise under `exercises/` includes:
- `README.md`: The real-world operational scenario, theory, required tasks, and verification steps.
- **Starter Template**: Scaffolding with `# TODO` markers where you write your code.
- `solution/`: A complete, reference solution with line-by-line explanatory comments.

### Workflow:
1. Navigate into an exercise directory:
   ```bash
   cd exercises/06-loops-and-conditionals
   ```
2. Read `README.md` to understand the challenge.
3. Open `playbook.yml` and implement your solution.
4. Run your playbook and verify the results using the verification commands.
5. Compare your implementation with `solution/playbook.yml`.

---

## 🧪 Automated Test & Validation Suite

Run the included automated verification runner at any time to validate your syntax, inventories, and playbooks:

```bash
# Validate entire repository
./scripts/validate.sh
```

---

## 📖 Additional Resources
- [Ansible Quick Reference Cheat Sheet](CHEAT_SHEET.md)
- [Official Ansible Documentation](https://docs.ansible.com/ansible/latest/)

