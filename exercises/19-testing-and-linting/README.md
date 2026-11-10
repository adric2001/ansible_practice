# Exercise 19: Testing, Linting, & Code Quality

## 🎯 Objective
Learn how to enforce production code quality, eliminate common anti-patterns using Ansible best practices, execute automated assertions (`ansible.builtin.assert`), and structure verification tests using Molecule concepts.

## 📖 Key Concepts

### 1. Common Anti-Patterns & Best Practices
| Anti-Pattern | Best Practice | Reason |
| :--- | :--- | :--- |
| `command: mkdir /foo` | `ansible.builtin.file: state=directory` | Native idempotency & proper state tracking |
| `copy: dest=/foo mode=644` | `ansible.builtin.copy: dest=/foo mode='0644'` | Unquoted numbers can parse as decimal integers, altering UNIX permissions |
| Module without FQCN (`template:`) | `ansible.builtin.template:` | Resolves unambiguous namespace in collections |
| Tasks without clear names | Meaningful descriptive task names | Clear debugging logs and test reports |
| Hardcoded absolute paths | Parameterized paths via variables | Reusability across test/prod environments |

### 2. Automated Assertions (`ansible.builtin.assert`)
Instead of manual inspection, assert post-conditions in code:
```yaml
- name: Verify service port is listening
  ansible.builtin.assert:
    that:
      - service_status.rc == 0
      - "'running' in service_output.stdout"
    fail_msg: "Health check assertion failed!"
    success_msg: "Service state validated."
```

### 3. Molecule Testing Workflow
Molecule tests roles through a lifecycle:
`dependency` -> `lint` -> `cleanup` -> `destroy` -> `syntax` -> `create` -> `prepare` -> `converge` -> `idempotence` -> `verify` -> `destroy`.

---

## 🏢 The Scenario
You are handed a legacy playbook `legacy_bad_playbook.yml` full of bugs and anti-patterns:
- Unquoted file modes.
- Shell commands instead of built-in file/copy modules.
- Missing FQCNs.
- Non-idempotent operations.
- No automated assertions.

Refactor it into `refactored_clean_playbook.yml` with a comprehensive `verify.yml` test suite!

---

## 📝 Tasks
1. Review `legacy_bad_playbook.yml`.
2. Implement `refactored_clean_playbook.yml` following standard linting and idempotency guidelines.
3. Run `verify.yml` to validate all system acceptance criteria.

---

## 🔍 Verification Commands

```bash
# Execute refactored playbook
ansible-playbook -i "localhost," -c local refactored_clean_playbook.yml

# Run automated verification suite
ansible-playbook -i "localhost," -c local verify.yml
```
