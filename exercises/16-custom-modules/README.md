# Exercise 16: Developing Custom Ansible Modules (Python)

## 🎯 Objective
Learn how to extend Ansible by writing a custom Python module using `AnsibleModule`, handling argument validation, idempotency, check mode (`--check`), and structured output return codes.

## 📖 Key Concepts

### 1. Where Custom Modules Live
Modules placed in a directory named `library/` adjacent to a playbook or inside a role (`roles/<role>/library/`) are automatically discovered by Ansible!

### 2. Anatomy of `AnsibleModule`
```python
from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        target_path=dict(type='str', required=True),
        max_files=dict(type='int', default=100),
        state=dict(type='str', choices=['present', 'absent'], default='present')
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # If check_mode: exit without modifying system
    if module.check_mode:
        module.exit_json(changed=False, msg="Check mode dry run")

    # Business logic...
    module.exit_json(changed=True, result_data={"processed": 42})
```

---

## 🏢 The Scenario
You need to develop a custom module `dir_quota_guard.py` in `library/`:
- **Parameters**:
  - `path`: Target directory path (string, required).
  - `max_files`: Maximum allowed files in directory (int, default 10).
  - `enforce_limit`: If true and count exceeds limit, delete excess oldest files (bool, default false).
- **Return Values**:
  - `changed`: True if files were deleted or state changed.
  - `current_file_count`: Total files counted.
  - `quota_exceeded`: Boolean flag.
  - `deleted_files`: List of filenames removed (if enforced).

---

## 📝 Tasks
1. Complete `library/dir_quota_guard.py`.
2. Run `playbook.yml` in both normal and check mode (`--check`).

---

## 🔍 Verification Commands

```bash
# Test custom module execution
ansible-playbook -i "localhost," -c local playbook.yml

# Test check mode
ansible-playbook -i "localhost," -c local playbook.yml --check
```
