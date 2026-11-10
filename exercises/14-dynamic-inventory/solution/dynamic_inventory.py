#!/usr/bin/env python3
"""
Reference Solution: Ansible Dynamic Inventory Script
Reads instances from cmdb_data.json and builds a fully dynamic Ansible inventory
with groups for environment, role, region, and populated _meta.hostvars.
"""

import sys
import os
import json
import argparse

def build_inventory():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    cmdb_path = os.path.join(script_dir, "..", "cmdb_data.json")
    if not os.path.exists(cmdb_path):
        cmdb_path = os.path.join(script_dir, "cmdb_data.json")

    with open(cmdb_path, "r", encoding="utf-8") as f:
        instances = json.load(f)

    inventory = {
        "_meta": {
            "hostvars": {}
        },
        "all": {
            "hosts": []
        }
    }

    def add_to_group(group_name, host):
        if group_name not in inventory:
            inventory[group_name] = {"hosts": [], "vars": {}}
        if host not in inventory[group_name]["hosts"]:
            inventory[group_name]["hosts"].append(host)

    for item in instances:
        hostname = item["hostname"]
        inventory["all"]["hosts"].append(hostname)

        # Dynamic grouping by tags
        env_grp = f"env_{item['environment'].replace('-', '_')}"
        role_grp = f"role_{item['role'].replace('-', '_')}"
        region_grp = f"region_{item['region'].replace('-', '_')}"

        add_to_group(env_grp, hostname)
        add_to_group(role_grp, hostname)
        add_to_group(region_grp, hostname)

        # Host-specific variables
        inventory["_meta"]["hostvars"][hostname] = {
            "ansible_host": item["private_ip"],
            "ansible_connection": "local",  # Configured for safe local testing
            "instance_id": item["id"],
            "deployment_env": item["environment"],
            "server_role": item["role"],
            "region": item["region"],
            "cpu_cores": item["cpu"],
            "memory_mb": item["memory_mb"]
        }

    return inventory

def main():
    parser = argparse.ArgumentParser(description="Ansible Dynamic Inventory Script")
    parser.add_argument("--list", action="store_true", help="List all inventory groups and hosts")
    parser.add_argument("--host", action="store", help="Get variables for specific host")
    args = parser.parse_args()

    inventory = build_inventory()

    if args.host:
        hostvars = inventory.get("_meta", {}).get("hostvars", {}).get(args.host, {})
        print(json.dumps(hostvars, indent=2))
    else:
        print(json.dumps(inventory, indent=2))

if __name__ == "__main__":
    main()
