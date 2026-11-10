#!/usr/bin/env bash
# Reference Solution: Ad-Hoc Operations Practice
set -e

TARGET="${1:-localhost}"
if [ "${TARGET}" = "localhost" ]; then
    INV="localhost,"
    EXTRA_OPTS="-c local"
    HOSTS="localhost"
else
    INV="../../lab/inventory.ini"
    EXTRA_OPTS=""
    HOSTS="all"
fi

echo "=== Reference Solutions: Ansible Ad-Hoc Commands ==="

# Task 1: Fleet Connectivity Ping
echo "1. Pinging hosts:"
ansible "${HOSTS}" -i "${INV}" ${EXTRA_OPTS} -m ansible.builtin.ping

# Task 2: Gather Specific Facts with Filter
echo "2. Querying OS distribution facts:"
ansible "${HOSTS}" -i "${INV}" ${EXTRA_OPTS} -m ansible.builtin.setup -a "filter=ansible_distribution*"

# Task 3: Disk Space Audit in Single-Line Output Format
echo "3. Disk audit (condensed single-line):"
ansible "${HOSTS}" -i "${INV}" ${EXTRA_OPTS} -o -m ansible.builtin.command -a "df -h"

# Task 4: Copy Inline Content to File with Strict Permissions
echo "4. Distribute alert message:"
ansible "${HOSTS}" -i "${INV}" ${EXTRA_OPTS} -m ansible.builtin.copy -a "content='SECURITY NOTICE: Scheduled maintenance tonight at 23:00 UTC\n' dest=/tmp/security_alert.txt mode=0644"

# Task 5: Check Mode / Dry-Run Creation of User
echo "5. Dry-run user verification (-C flag):"
ansible "${HOSTS}" -i "${INV}" ${EXTRA_OPTS} -C -m ansible.builtin.user -a "name=auditor uid=1500 state=present"

# Task 6: Audit File Existence / State
echo "6. Checking file status with stat module:"
ansible "${HOSTS}" -i "${INV}" ${EXTRA_OPTS} -m ansible.builtin.stat -a "path=/tmp/security_alert.txt"

# Task 7: Query Memory Facts
echo "7. Memory facts:"
ansible "${HOSTS}" -i "${INV}" ${EXTRA_OPTS} -m ansible.builtin.setup -a "filter=ansible_memtotal_mb"

# Task 8: Cleanup temporary alert file
echo "8. Cleaning up test file:"
ansible "${HOSTS}" -i "${INV}" ${EXTRA_OPTS} -m ansible.builtin.file -a "path=/tmp/security_alert.txt state=absent"

echo "=== All Ad-Hoc Solutions Completed Successfully! ==="
