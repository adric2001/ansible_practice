# Exercise 21: Asynchronous Execution & Status Polling (`async` & `poll`)

## 🎯 Objective
Master asynchronous operations in Ansible to execute long-running background tasks without blocking, perform concurrent operations, and poll for task completion using `ansible.builtin.async_status`.

## 📖 Key Concepts

### 1. Synchronous vs Asynchronous
- By default, Ansible tasks are synchronous: Ansible blocks until each task completes on all hosts before proceeding.
- **Asynchronous Execution (`async: <seconds>`)**:
  - `async: 60, poll: 5`: Waits up to 60 seconds, polling every 5 seconds.
  - `async: 300, poll: 0`: **Fire-and-forget**. Ansible kicks off the job in the background and immediately moves to the next task!

### 2. Checking Job Status (`async_status`)
When running with `poll: 0`, the task returns `ansible_job_id`. You can query its progress later:
```yaml
- name: Check background job status
  ansible.builtin.async_status:
    jid: "{{ background_job.ansible_job_id }}"
  register: job_result
  until: job_result.finished
  retries: 30
  delay: 2
```

---

## 🏢 The Scenario
You are orchestrating a system maintenance window:
1. Kick off a time-consuming simulation task in the background using `async: 60, poll: 0`.
2. While the background task is running, execute 2 fast tasks (cache cleanup and directory setup).
3. Poll the background job using `ansible.builtin.async_status` until it signals `finished: 1`.

---

## 📝 Tasks
Open `playbook.yml` and implement the async pattern.

---

## 🔍 Verification Commands

```bash
# Execute against localhost
ansible-playbook -i "localhost," -c local playbook.yml
```

