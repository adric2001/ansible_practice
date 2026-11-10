#!/usr/bin/env bash
# Ad-Hoc Operations Practice Script
# Fill in each function with the appropriate 'ansible' CLI command.

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

# Task 1: Ping all hosts
task1_ping() {
    echo ">> Running Task 1: Ping hosts..."
    # TODO: Write ansible ad-hoc command to ping $HOSTS
    ansible "${HOSTS}" -i "${INV}" ${EXTRA_OPTS} -m ping
}

# Task 2: Gather only distribution facts
task2_distribution_facts() {
    echo ">> Running Task 2: Distribution Facts..."
    # TODO: Use setup module with filter="ansible_distribution*"
}

# Task 3: Check disk space in one-line format
task3_disk_audit() {
    echo ">> Running Task 3: Disk audit (one-line)..."
    # TODO: Run 'df -h' with -o (one-line format)
}

# Task 4: Copy a file with permissions 0644
task4_copy_file() {
    echo ">> Running Task 4: Copy security alert..."
    # TODO: Use copy module to write content 'SECURITY NOTICE: Maintenance tonight' to /tmp/security_alert.txt
}

# Task 5: Check if user 'auditor' exists using check mode
task5_check_user() {
    echo ">> Running Task 5: User verification (dry-run)..."
    # TODO: Use user module in check mode (-C) to check for user 'auditor'
}

# Task 6: Audit service state
task6_service_state() {
    echo ">> Running Task 6: Check service state..."
    # TODO: Query service facts or check service status
}

echo "=== Executing Ad-Hoc Challenges ==="
task1_ping
# Uncomment tasks as you complete them:
# task2_distribution_facts
# task3_disk_audit
# task4_copy_file
# task5_check_user
# task6_service_state
