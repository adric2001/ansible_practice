# Exercise 18: Developing Custom Callback Plugins

## 🎯 Objective
Learn how to capture playbook execution telemetry, format terminal outputs, and build automated audit logging by developing a custom Ansible Callback Plugin in Python.

## 📖 Key Concepts

### 1. What are Callback Plugins?
Callback plugins intercept events throughout the playbook execution lifecycle:
- When a play starts: `v2_playbook_on_start`
- When a task finishes: `v2_runner_on_ok`, `v2_runner_on_failed`, `v2_runner_on_skipped`
- When the entire playbook finishes: `v2_playbook_on_stats`

### 2. Where Callback Plugins Live
Place Python callback files in `callback_plugins/` adjacent to a playbook or configured in `ansible.cfg` under `callback_plugins`.

### 3. Enabling Custom Callbacks
In `ansible.cfg`:
```ini
[defaults]
callbacks_enabled = timer, custom_audit_logger
```
Or via environment variable:
```bash
export ANSIBLE_CALLBACKS_ENABLED=custom_audit_logger
```

---

## 🏢 The Scenario
You need to develop a custom callback plugin `custom_audit_logger.py` that:
1. Intercepts each task completion.
2. Measures task execution time.
3. Automatically appends a JSON line to `/tmp/ansible_callback_audit.jsonl` containing:
   - `timestamp`
   - `task_name`
   - `host`
   - `status` (`OK`, `FAILED`, `SKIPPED`)
   - `duration_seconds`
4. On playbook completion, appends a final summary recap object.

---

## 📝 Tasks
1. Complete `callback_plugins/custom_audit_logger.py`.
2. Execute `playbook.yml` with the callback enabled.
3. Verify the generated JSON log.

---

## 🔍 Verification Commands

```bash
# Execute playbook with custom callback
ANSIBLE_CALLBACKS_ENABLED=custom_audit_logger ansible-playbook -i "localhost," -c local playbook.yml

# Inspect the generated audit log
cat /tmp/ansible_callback_audit.jsonl
```

