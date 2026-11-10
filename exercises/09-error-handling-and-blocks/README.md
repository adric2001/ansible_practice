# Exercise 09: Error Handling, Blocks, & Rollbacks

## 🎯 Objective
Master fault tolerance, automated recovery, and structured exception handling using Ansible's `block`, `rescue`, and `always` statements.

## 📖 Key Concepts

### 1. The Block / Rescue / Always Pattern
Similar to `try / catch / finally` in programming languages:
- **`block`**: Contains the primary tasks expected to run under normal conditions.
- **`rescue`**: Executes **only if** one of the tasks inside `block` fails (`failed: true`).
- **`always`**: Guaranteed to run under all conditions (whether `block` succeeded or `rescue` executed).

### 2. Error Flags
- `ignore_errors: true`: Task continues even if rc != 0, but does not trigger `rescue`.
- `any_errors_fatal: true`: If any single host fails, immediately abort the play on all hosts.
- `failed_when`: Custom conditional triggering failure based on stdout, stderr, or return code.

---

## 🏢 The Scenario
You are automating a critical database upgrade:
1. **Normal Flow (`block`)**:
   - Take a snapshot of the active database directory (`/tmp/ansible_db_lab/data/`).
   - Attempt to execute a new database schema migration script.
   - (For testing, the migration script will simulate a failure).
2. **Recovery Flow (`rescue`)**:
   - Catch the failure.
   - Restore the database files from the snapshot backup.
   - Record an incident flag `/tmp/ansible_db_lab/ROLLBACK_EXECUTED`.
3. **Guaranteed Cleanup (`always`)**:
   - Delete temporary migration lockfiles `/tmp/ansible_db_lab/*.lock`.
   - Record an audit entry in `/tmp/ansible_db_lab/audit.log`.

---

## 📝 Tasks
Open `playbook.yml` and implement the `block`, `rescue`, and `always` sections.

---

## 🔍 Verification Commands

```bash
# Execute against localhost
ansible-playbook -i "localhost," -c local playbook.yml

# Verify rollback and audit log
ls -la /tmp/ansible_db_lab/
cat /tmp/ansible_db_lab/audit.log
```
