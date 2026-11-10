# Exercise 07: Handlers & Notifications

## 🎯 Objective
Understand the handler lifecycle, notification mechanism (`notify`), handler deduplication, topic broadcasting (`listen`), and forced early execution using `meta: flush_handlers`.

## 📖 Key Concepts

### 1. Handler Fundamentals
- Handlers are special tasks that only run when triggered by a `notify` directive from another task.
- Handlers run **only if** the notifying task causes a change (`changed: true`).
- By default, handlers run once at the very end of the play, regardless of how many tasks notified them (deduplication).

### 2. Handler Topics (`listen`)
Instead of referencing a handler by its specific task name, handlers can listen to a generic topic:
```yaml
handlers:
  - name: Reload Nginx
    ansible.builtin.service:
      name: nginx
      state: reloaded
    listen: "restart web services"

  - name: Reload Gunicorn
    ansible.builtin.service:
      name: gunicorn
      state: reloaded
    listen: "restart web services"
```
Notifying `"restart web services"` triggers both handlers!

### 3. Flushing Handlers (`meta: flush_handlers`)
Sometimes a service MUST be restarted immediately in the middle of a play (e.g., database must be restarted with new auth configs before application migrations can connect).
```yaml
- name: Flush handlers now
  ansible.builtin.meta: flush_handlers
```

---

## 🏢 The Scenario
You are deploying a web service config update in `/tmp/ansible_handlers_lab`:
1. Task A writes the main server config.
2. Task B writes a virtual host config. Both notify `restart web server`.
3. Use `meta: flush_handlers` so the restart happens *immediately* before Task C runs.
4. Task C runs a synthetic health probe checking that the new config is active.
5. Demonstrate that running the playbook a second time (when nothing changes) triggers **zero** handlers!

---

## 📝 Tasks
Open `playbook.yml` and complete the handler configuration.

---

## 🔍 Verification Commands

```bash
# 1. First run: handlers will execute
ansible-playbook -i "localhost," -c local playbook.yml

# 2. Second run: idempotency check (no handlers should fire)
ansible-playbook -i "localhost," -c local playbook.yml
```
