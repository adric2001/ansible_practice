# Exercise 15: Strategies, Delegation, & Zero-Downtime Rolling Updates

## 🎯 Objective
Master rolling deployment patterns using `serial`, `max_fail_percentage`, `delegate_to`, and `run_once` to orchestrate zero-downtime application upgrades across a cluster.

## 📖 Key Concepts

### 1. Controlling Concurrency with `serial`
By default, Ansible runs a task on all hosts in parallel (up to `forks`). `serial` restricts execution to batches:
```yaml
- name: Rolling Deployment
  hosts: webservers
  serial:
    - 1        # Canary batch (deploy to 1 host first)
    - "50%"    # Half the fleet
    - "100%"   # Remaining fleet
  max_fail_percentage: 0  # Abort if ANY host fails in a batch!
```

### 2. Task Delegation (`delegate_to`)
Execute a task on a different machine while preserving the context and variables of the current host:
```yaml
- name: Remove host from load balancer pool
  ansible.builtin.command: "/usr/local/bin/drain_node.sh {{ inventory_hostname }}"
  delegate_to: loadbalancer_host
```

### 3. Single Execution (`run_once`)
Run a task only once across the entire batch/play (e.g. running a database migration once instead of N times per host).

---

## 🏢 The Scenario
You have 4 web servers behind a load balancer (`/tmp/ansible_rolling_lab/`):
1. Use `serial: [1, 2, "100%"]` for progressive canary deployment.
2. For each host in the batch:
   - Delegate a task to `localhost` to remove the host from the load balancer pool.
   - Simulate deploying the application update.
   - Run a health check probe against the updated host.
   - Delegate a task to `localhost` to re-enable the host in the load balancer pool.
3. Use `run_once: true` to send a single Slack/notification webhook at the start.

---

## 📝 Tasks
Open `playbook.yml` and implement the rolling update workflow.

---

## 🔍 Verification Commands

```bash
# Execute rolling deployment
ansible-playbook -i inventory.ini playbook.yml
```

