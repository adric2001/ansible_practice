# Exercise 03: Playbook Basics & Idempotency

## 🎯 Objective
Understand core playbook structure, play declarations, and the principle of **idempotency** — ensuring that executing a playbook multiple times results in identical system state without unintended changes or errors.

## 📖 Key Concepts
- **Playbook Structure**:
  - `name`: Human-readable description of the play.
  - `hosts`: Host pattern specifying target machines.
  - `become`: Flag indicating whether privilege escalation is required.
  - `gather_facts`: Boolean to enable/disable automated discovery of remote node facts.
  - `tasks`: Ordered list of tasks to execute sequentially.
- **Idempotency**: An operation is idempotent if the result of executing it once is identical to the result of executing it multiple times.
  - Non-idempotent task example: `ansible.builtin.shell: echo "foo" >> /tmp/file` (appends every run).
  - Idempotent task example: `ansible.builtin.lineinfile: path=/tmp/file line="foo" state=present` (ensures line exists once).
- **Key Modules**:
  - `ansible.builtin.file`: Manage directory structures, permissions, symlinks, and deletion.
  - `ansible.builtin.copy`: Deploy files or inline text content.
  - `ansible.builtin.lineinfile`: Ensure particular lines are present or absent in a configuration file.

---

## 🏢 The Scenario
You need to write a baseline system configuration playbook targeting `/tmp/practice_baseline/` that performs:
1. Creates directory structure:
   - `/tmp/practice_baseline/config` (mode: `0755`)
   - `/tmp/practice_baseline/secure` (mode: `0700`)
   - `/tmp/practice_baseline/logs`   (mode: `0775`)
2. Deploys `/tmp/practice_baseline/config/motd` containing an authorized access warning banner.
3. Generates `/tmp/practice_baseline/config/security.conf` and uses `lineinfile` with regex replacement to enforce:
   - `MAX_FAILED_ATTEMPTS=3`
   - `SESSION_TIMEOUT_SECONDS=900`
   - `ALLOW_ROOT_SSH=no`
4. Creates a symlink `/tmp/practice_baseline/current_config` pointing to `/tmp/practice_baseline/config`.

---

## 📝 Tasks
Open `playbook.yml` and implement the tasks according to the specification.

---

## 🔍 Verification Commands

Test your playbook and verify idempotency:
```bash
# 1. First run: should execute and report "changed: X"
ansible-playbook -i "localhost," -c local playbook.yml

# 2. Second run: MUST report "changed=0" to prove idempotency!
ansible-playbook -i "localhost," -c local playbook.yml

# 3. Dry-run with diff output:
ansible-playbook -i "localhost," -c local playbook.yml --check --diff
```
