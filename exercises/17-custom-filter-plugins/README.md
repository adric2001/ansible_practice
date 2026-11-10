# Exercise 17: Developing Custom Jinja2 Filter Plugins

## 🎯 Objective
Learn how to extend Ansible's templating engine by developing custom Jinja2 filter plugins written in Python to perform custom data transformations.

## 📖 Key Concepts

### 1. Where Filter Plugins Live
Filter plugins placed in a directory named `filter_plugins/` adjacent to a playbook or inside a role are automatically loaded by Ansible.

### 2. Anatomy of a Filter Plugin
A filter plugin is a Python module implementing a class `FilterModule` with a `filters(self)` method returning a dictionary mapping filter names to Python callable functions:

```python
class FilterModule(object):
    def filters(self):
        return {
            'custom_filter_name': self.custom_transform,
            'another_filter': self.another_func
        }

    def custom_transform(self, value, arg1=None):
        # Transform data
        return transformed_value
```

---

## 🏢 The Scenario
You need to build three custom filters in `filter_plugins/custom_filters.py`:
1. `bytes_to_human(bytes_val, unit='auto')`: Converts raw bytes into human readable format (`1073741824` -> `"1.00 GB"`).
2. `mask_secret(secret_str, show_last=4)`: Masks sensitive tokens, showing only the last N characters (`"sk_live_998877665544"` -> `"************5544"`).
3. `split_and_trim(string_val, delimiter=',')`: Splits a delimited string, strips whitespace from each element, and filters empty strings.

---

## 📝 Tasks
1. Complete `filter_plugins/custom_filters.py`.
2. Complete `playbook.yml` to apply and test the custom filters.

---

## 🔍 Verification Commands

```bash
# Execute against localhost
ansible-playbook -i "localhost," -c local playbook.yml
```
