# Exercise 08: Jinja2 Templating Mastery

## 🎯 Objective
Master the art of dynamic configuration generation using Jinja2 templates, filter pipelines, loop control, whitespace trimming, and template validation.

## 📖 Key Concepts

### 1. Template Basics
- Delimiters:
  - `{{ variable }}`: Expression interpolation.
  - `{% statement %}`: Logic (if, for, set).
  - `{# comment #}`: Jinja2 comment (omitted from rendered output).
  - `{%-` and `-%}`: Strip leading / trailing whitespace and newlines.

### 2. Powerful Jinja2 Filters
- Default fallback: `{{ db_port | default(5432) }}`
- Case manipulation: `{{ env_name | upper }}`
- Serialization: `{{ config_dict | to_nice_json }}`, `{{ config_dict | to_nice_yaml }}`
- List processing:
  - `{{ upstream_servers | map(attribute='ip') | join(', ') }}`
  - `{{ server_tags | unique | sort | list }}`

### 3. Template Validation
Before copying the rendered file into place, Ansible can run a test command using `%s` as the placeholder for the temporary rendered file:
```yaml
ansible.builtin.template:
  src: nginx.conf.j2
  dest: /etc/nginx/nginx.conf
  validate: "nginx -t -c %s"
```

---

## 🏢 The Scenario
You need to generate a dynamic Nginx reverse proxy configuration (`/tmp/ansible_template_lab/nginx.conf`) for a multi-backend microservice:
1. Upstream pool with dynamic servers (IP and port).
2. Health check interval and timeout from variables with sensible `default()` values.
3. Conditional SSL server block (only included if `ssl_enabled: true`).
4. Location routing rules generated dynamically by looping over an `endpoints` list of dictionaries.
5. Automatic header stamping: `# Managed by Ansible - Host: {{ inventory_hostname }} - Generated on: {{ ansible_date_time.iso8601 | default('N/A') }}`.

---

## 📝 Tasks
1. Complete `templates/nginx.conf.j2`.
2. Complete `playbook.yml` to render the template and validate the resulting syntax.

---

## 🔍 Verification Commands

```bash
# Run against localhost
ansible-playbook -i "localhost," -c local playbook.yml

# Inspect rendered configuration
cat /tmp/ansible_template_lab/nginx.conf
```
