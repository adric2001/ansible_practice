#!/usr/bin/env python3
"""
Starter Dynamic Inventory Script
Reads CMDB data from cmdb_data.json and produces Ansible-compliant inventory JSON.
"""

import sys
import os
import json
import argparse

def build_inventory():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    cmdb_path = os.path.join(script_dir, "cmdb_data.json")

    with open(cmdb_path, "r") as f:
        instances = json.load(f)

    inventory = {
        "_meta": {
            "hostvars": {}
        },
        "all": {
            "hosts": []
        }
    }

    # TODO: Loop over instances from CMDB and populate:
    # 1. Groups by environment (e.g. prod, staging)
    # 2. Groups by role (e.g. web, database)
    # 3. Groups by region (e.g. us-east, eu-west)
    # 4. _meta.hostvars[hostname] with ansible_host, cpu, memory_mb, etc.

    return inventory

def main():
    parser = argparse.ArgumentParser(description="Ansible Dynamic Inventory Script")
    parser.add_argument("--list", action="store_true", help="List all active inventory groups and hosts")
    parser.add_argument("--host", action="store", help="Get variables for specific host")
    args = parser.parse_args()

    inventory = build_inventory()

    if args.list:
        print(json.dumps(inventory, indent=2))
    elif args.host:
        hostvars = inventory.get("_meta", {}).get("hostvars", {}).get(args.host, {})
        print(json.dumps(hostvars, indent=2))
    else:
        print(json.dumps(inventory, indent=2))

if __name__ == "__main__":
    main()
