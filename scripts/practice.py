#!/usr/bin/env python3
"""
Interactive Ansible Practice CLI
Browse exercises, view instructions, run tests, and check solutions.
"""

import os
import sys
import subprocess
import glob

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXERCISES_DIR = os.path.join(REPO_ROOT, "exercises")

CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

def get_exercises():
    dirs = sorted([d for d in os.listdir(EXERCISES_DIR) if os.path.isdir(os.path.join(EXERCISES_DIR, d)) and not d.startswith(".")])
    return dirs

def list_exercises():
    exercises = get_exercises()
    print(f"\n{BOLD}{CYAN}=== Available Ansible Practice Exercises ({len(exercises)} Total) ==={RESET}")
    for idx, name in enumerate(exercises, 1):
        print(f"  {BOLD}{idx:2d}.{RESET} {name}")
    print()

def show_readme(ex_name):
    readme_path = os.path.join(EXERCISES_DIR, ex_name, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print(f"README not found for {ex_name}")

def test_exercise(ex_name):
    ex_path = os.path.join(EXERCISES_DIR, ex_name)
    sol_playbook = os.path.join(ex_path, "solution", "playbook.yml")
    if not os.path.exists(sol_playbook):
        sol_playbook = os.path.join(ex_path, "solution", "site.yml")

    if not os.path.exists(sol_playbook):
        print(f"No solution playbook found in {ex_name}")
        return

    print(f"\n{BOLD}Running validation on {ex_name}...{RESET}")
    cmd = ["ansible-playbook", "--syntax-check", sol_playbook]
    # Check for inventory or vault
    inv_file = os.path.join(ex_path, "inventory.ini")
    if os.path.exists(inv_file):
        cmd.extend(["-i", inv_file])
    vault_pass = os.path.join(ex_path, ".vault_password")
    if os.path.exists(vault_pass):
        cmd.extend(["--vault-password-file", vault_pass])

    res = subprocess.run(cmd)
    if res.returncode == 0:
        print(f"{GREEN}✓ Syntax check passed!{RESET}")
    else:
        print(f"{YELLOW}✗ Syntax check failed!{RESET}")

def main():
    if len(sys.argv) < 2:
        list_exercises()
        print(f"Usage:")
        print(f"  python3 scripts/practice.py list")
        print(f"  python3 scripts/practice.py show <number or name>")
        print(f"  python3 scripts/practice.py test <number or name>")
        print(f"  python3 scripts/practice.py validate-all\n")
        return

    action = sys.argv[1].lower()
    exercises = get_exercises()

    if action == "list":
        list_exercises()
    elif action == "validate-all":
        subprocess.run([os.path.join(REPO_ROOT, "scripts", "validate.sh")])
    elif action in ["show", "read", "view"]:
        if len(sys.argv) < 3:
            print("Please specify an exercise number or name.")
            return
        arg = sys.argv[2]
        match = None
        if arg.isdigit():
            idx = int(arg) - 1
            if 0 <= idx < len(exercises):
                match = exercises[idx]
        else:
            for ex in exercises:
                if arg in ex:
                    match = ex
                    break
        if match:
            show_readme(match)
        else:
            print(f"Exercise '{arg}' not found.")
    elif action in ["test", "check"]:
        if len(sys.argv) < 3:
            print("Please specify an exercise number or name.")
            return
        arg = sys.argv[2]
        match = None
        if arg.isdigit():
            idx = int(arg) - 1
            if 0 <= idx < len(exercises):
                match = exercises[idx]
        else:
            for ex in exercises:
                if arg in ex:
                    match = ex
                    break
        if match:
            test_exercise(match)
        else:
            print(f"Exercise '{arg}' not found.")

if __name__ == "__main__":
    main()

