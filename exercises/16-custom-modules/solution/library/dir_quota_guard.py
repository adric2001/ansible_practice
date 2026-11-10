#!/usr/bin/python
"""
Reference Solution: Custom Ansible Module dir_quota_guard
Audits directory file count against quota, reports metrics, and optionally enforces limits.
"""

from ansible.module_utils.basic import AnsibleModule
import os
import glob

DOCUMENTATION = r'''
---
module: dir_quota_guard
short_description: Monitor and enforce directory file quota limits
description:
  - Scans target directory, calculates total file count and size.
  - Reports quota status and optionally removes oldest files exceeding limit.
options:
  path:
    description: Absolute path of target directory to monitor.
    required: true
    type: str
  max_files:
    description: Maximum number of files permitted before quota breach.
    default: 10
    type: int
  enforce_limit:
    description: Whether to actively prune oldest excess files when limit is exceeded.
    default: false
    type: bool
author:
  - Ansible Practice Team
'''

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        max_files=dict(type='int', default=10),
        enforce_limit=dict(type='bool', default=False)
    )

    result = dict(
        changed=False,
        current_file_count=0,
        quota_exceeded=False,
        deleted_files=[],
        total_size_bytes=0
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    target_path = os.path.expanduser(module.params['path'])
    max_files = module.params['max_files']
    enforce = module.params['enforce_limit']

    if not os.path.exists(target_path):
        module.fail_json(msg=f"Directory does not exist: {target_path}", **result)

    if not os.path.isdir(target_path):
        module.fail_json(msg=f"Path is not a directory: {target_path}", **result)

    # List regular files sorted by mtime (oldest first)
    entries = []
    total_size = 0
    for name in os.listdir(target_path):
        full_path = os.path.join(target_path, name)
        if os.path.isfile(full_path):
            stat = os.stat(full_path)
            entries.append((full_path, stat.st_mtime, stat.st_size))
            total_size += stat.st_size

    entries.sort(key=lambda x: x[1])  # Sort by modification timestamp
    count = len(entries)

    result['current_file_count'] = count
    result['total_size_bytes'] = total_size
    result['quota_exceeded'] = count > max_files

    if count > max_files and enforce:
        excess = count - max_files
        to_delete = entries[:excess]

        if module.check_mode:
            result['changed'] = True
            result['deleted_files'] = [os.path.basename(p[0]) for p in to_delete]
            module.exit_json(**result)

        deleted = []
        for file_path, _, size in to_delete:
            try:
                os.remove(file_path)
                deleted.append(os.path.basename(file_path))
                total_size -= size
            except OSError as e:
                module.fail_json(msg=f"Failed to remove {file_path}: {str(e)}", **result)

        result['changed'] = len(deleted) > 0
        result['deleted_files'] = deleted
        result['current_file_count'] = count - len(deleted)
        result['total_size_bytes'] = total_size
        result['quota_exceeded'] = result['current_file_count'] > max_files

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
