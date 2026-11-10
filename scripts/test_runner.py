#!/usr/bin/env python3
"""
Ansible Practice Suite Test & Validation Runner
Validates YAML structure, Python plugin syntax, inventory parsing, and playbook syntax.
"""

import os
import sys
import glob
import subprocess
import py_compile

try:
    import yaml
except ImportError:
    yaml = None

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO_ROOT)

os.environ["ANSIBLE_LOCAL_TEMP"] = os.environ.get("ANSIBLE_LOCAL_TEMP", "/tmp/ansible-local")
os.environ["ANSIBLE_REMOTE_TEMP"] = os.environ.get("ANSIBLE_REMOTE_TEMP", "/tmp/ansible-remote")
os.makedirs(os.environ["ANSIBLE_LOCAL_TEMP"], exist_ok=True)
os.makedirs(os.environ["ANSIBLE_REMOTE_TEMP"], exist_ok=True)

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"
BOLD = "\033[1m"

passed_count = 0
failed_count = 0

def log_pass(msg):
    global passed_count
    passed_count += 1
    print(f"  {GREEN}✓ PASS{RESET} {msg}")

def log_fail(msg, error=""):
    global failed_count
    failed_count += 1
    print(f"  {RED}✗ FAIL{RESET} {msg}")
    if error:
        print(f"    {YELLOW}{error.strip()}{RESET}")

def test_yaml_files():
    print(f"\n{BOLD}{BLUE}[1/4] Validating YAML File Syntax...{RESET}")
    for root, _, files in os.walk(REPO_ROOT):
        if ".git" in root or "venv" in root:
            continue
        for f in sorted(files):
            if f.endswith((".yml", ".yaml")) and not f.endswith(".j2"):
                path = os.path.relpath(os.path.join(root, f), REPO_ROOT)
                # Skip vault encrypted files
                try:
                    with open(path, "r", encoding="utf-8") as yf:
                        content = yf.read()
                        if "$ANSIBLE_VAULT" in content:
                            continue
                        yaml.safe_load(content)
                    log_pass(path)
                except Exception as e:
                    log_fail(path, str(e))

def test_python_syntax():
    print(f"\n{BOLD}{BLUE}[2/4] Validating Python Scripts & Plugins...{RESET}")
    for root, _, files in os.walk(REPO_ROOT):
        if ".git" in root or "venv" in root:
            continue
        for f in sorted(files):
            if f.endswith(".py"):
                path = os.path.relpath(os.path.join(root, f), REPO_ROOT)
                try:
                    py_compile.compile(path, doraise=True)
                    log_pass(path)
                except py_compile.PyCompileError as e:
                    log_fail(path, str(e))

def test_inventories():
    print(f"\n{BOLD}{BLUE}[3/4] Validating Inventory Parsability...{RESET}")
    inventories = [
        "lab/inventory.ini",
        "lab/inventory.yml",
        "exercises/01-inventory-fundamentals/solution/inventory.ini",
        "exercises/01-inventory-fundamentals/solution/inventory.yml",
        "exercises/05-variables-facts-precedence/inventory.ini",
        "exercises/11-multitier-application-stack/inventory.ini",
        "exercises/15-strategies-delegation-rolling-updates/inventory.ini",
        "exercises/14-dynamic-inventory/solution/dynamic_inventory.py"
    ]
    for inv in inventories:
        if not os.path.exists(inv):
            continue
        cmd = ["ansible-inventory", "-i", inv, "--list"]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if res.returncode == 0:
            log_pass(f"Inventory: {inv}")
        else:
            log_fail(f"Inventory: {inv}", res.stderr)

def test_playbook_syntax():
    print(f"\n{BOLD}{BLUE}[4/4] Validating Solution Playbooks Syntax...{RESET}")
    playbooks = [
        ("exercises/03-playbook-basics-idempotency/solution/playbook.yml", []),
        ("exercises/04-package-and-service-management/solution/playbook.yml", []),
        ("exercises/05-variables-facts-precedence/solution/playbook.yml", ["-i", "exercises/05-variables-facts-precedence/inventory.ini"]),
        ("exercises/06-loops-and-conditionals/solution/playbook.yml", []),
        ("exercises/07-handlers-and-notifications/solution/playbook.yml", []),
        ("exercises/08-jinja2-templating/solution/playbook.yml", []),
        ("exercises/09-error-handling-and-blocks/solution/playbook.yml", []),
        ("exercises/10-role-architecture/solution/playbook.yml", []),
        ("exercises/11-multitier-application-stack/solution/site.yml", ["-i", "exercises/11-multitier-application-stack/inventory.ini"]),
        ("exercises/12-ansible-vault-security/solution/playbook.yml", ["--vault-password-file", "exercises/12-ansible-vault-security/.vault_password"]),
        ("exercises/13-collections-and-galaxy/solution/playbook.yml", []),
        ("exercises/14-dynamic-inventory/solution/playbook.yml", ["-i", "exercises/14-dynamic-inventory/solution/dynamic_inventory.py"]),
        ("exercises/15-strategies-delegation-rolling-updates/solution/playbook.yml", ["-i", "exercises/15-strategies-delegation-rolling-updates/inventory.ini"]),
        ("exercises/16-custom-modules/solution/playbook.yml", []),
        ("exercises/17-custom-filter-plugins/solution/playbook.yml", []),
        ("exercises/18-custom-callback-plugins/solution/playbook.yml", []),
        ("exercises/19-testing-and-linting/solution/refactored_clean_playbook.yml", []),
        ("exercises/19-testing-and-linting/solution/verify.yml", []),
        ("exercises/20-security-hardening-and-compliance/solution/playbook.yml", [])
    ]
    for pb, extra_args in playbooks:
        if not os.path.exists(pb):
            continue
        cmd = ["ansible-playbook", "--syntax-check", pb] + extra_args
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if res.returncode == 0:
            log_pass(f"Playbook: {pb}")
        else:
            log_fail(f"Playbook: {pb}", res.stderr)

def main():
    print(f"{BOLD}=================================================================={RESET}")
    print(f"{BOLD}           Ansible Practice Suite Test & Verification             {RESET}")
    print(f"{BOLD}=================================================================={RESET}")
    test_yaml_files()
    test_python_syntax()
    test_inventories()
    test_playbook_syntax()

    print(f"\n{BOLD}=================================================================={RESET}")
    print(f"Results: {GREEN}{passed_count} passed{RESET}, {RED if failed_count else GREEN}{failed_count} failed{RESET}")
    print(f"{BOLD}=================================================================={RESET}\n")

    sys.exit(0 if failed_count == 0 else 1)

if __name__ == "__main__":
    main()
