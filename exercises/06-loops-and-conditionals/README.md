# Exercise 06: Loops, Conditionals, & Task Control

## 🎯 Objective
Master advanced looping constructs, clean output filtering with `loop_control.label`, conditional branching with `when`, custom failure/change detection with `failed_when` and `changed_when`, and retry polling with `until`.

## 📖 Key Concepts

### 1. Modern Loops (`loop`)
- Iterate lists: `loop: [ 'item1', 'item2' ]`
- Iterate dictionaries or hashes: `loop: "{{ users_list }}"`
- `loop_control`:
  - `label`: Prevents huge dicts from flooding the console by displaying only a specific field (e.g., `label: "{{ item.name }}"`).
  - `index_var`: Exposes the 0-indexed loop position as a variable.
  - `pause`: Adds delay between loop iterations.

### 2. Conditionals (`when`)
- Single condition: `when: environment_type == 'production'`
- Multiple conditions (AND logic):
  ```yaml
  when:
    - server_role == 'web'
    - ansible_facts['distribution'] == 'Ubuntu'
  ```
- OR logic: `when: is_primary or backup_enabled`
- Variable tests: `when: custom_port is defined`, `when: app_debug | bool`

### 3. Task Status Overrides
- `changed_when: false`: Prevents commands that only read or query state from registering as `changed`.
- `failed_when`: Custom criteria for determining task failure (e.g. `failed_when: "'CRITICAL' in result.stdout"`).

### 4. Polling with `until`
- Repeat a task until a condition evaluates to true:
  ```yaml
  until: result.rc == 0
  retries: 5
  delay: 2
  ```

---

## 🏢 The Scenario
You are orchestrating an automated environment onboarding:
1. Provision a list of user accounts defined in a data structure with varying roles (`admin`, `developer`, `viewer`), custom shells, and optional supplementary groups.
2. Only users with `role: admin` or `role: developer` should be created.
3. Clean loop output so only the user's username is printed in stdout using `loop_control.label`.
4. Run a command that checks mock service health; use `changed_when: false` so it remains idempotent.
5. Poll a mock status file with `until` until it contains the word `"READY"`.

---

## 📝 Tasks
Open `playbook.yml` and complete the starter code.

---

## 🔍 Verification Commands

```bash
# Execute against localhost
ansible-playbook -i "localhost," -c local playbook.yml
```

