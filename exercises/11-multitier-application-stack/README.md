# Exercise 11: Multi-Tier Application Architecture

## 🎯 Objective
Learn how to design multi-play playbooks to orchestrate multi-tier architectures (Database -> Application -> Load Balancer) where tiers depend on data from other tiers.

## 📖 Key Concepts

### 1. Multi-Play Architecture
In complex deployments, different tiers run different roles on different host groups:
```yaml
# Play 1: Database Tier
- name: Deploy Database Tier
  hosts: dbservers
  roles: [ role_db ]

# Play 2: Application Tier
- name: Deploy App Tier
  hosts: appservers
  roles: [ role_app ]

# Play 3: Load Balancer Tier
- name: Deploy Load Balancer Tier
  hosts: loadbalancers
  roles: [ role_lb ]
```

### 2. Cross-Play Variable Sharing
The Load Balancer needs to know the IP addresses of all hosts in `appservers`. It queries them via the `groups` and `hostvars` magic variables:
```jinja2
{% for host in groups['appservers'] %}
server {{ hostvars[host]['ansible_host'] }}:{{ app_port }};
{% endfor %}
```

---

## 🏢 The Scenario
You are deploying a 3-tier microservice:
1. **Tier 1 (DB Tier)**: Generates a database connection endpoint and secret token in `/tmp/multitier_lab/db/`.
2. **Tier 2 (App Tier)**: Reads the DB connection string from Tier 1 facts and provisions app service configs in `/tmp/multitier_lab/app/`.
3. **Tier 3 (Proxy/LB Tier)**: Configures Nginx reverse proxy routes balancing requests across all app servers.

---

## 📝 Tasks
1. Examine the roles in `roles/`.
2. Complete `site.yml` to orchestrate all three plays in sequence.

---

## 🔍 Verification Commands

```bash
# Execute multi-play deployment against inventory
ansible-playbook -i inventory.ini site.yml
```
