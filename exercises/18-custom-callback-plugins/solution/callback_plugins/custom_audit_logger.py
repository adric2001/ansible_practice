#!/usr/bin/python
"""
Reference Solution: Custom Callback Plugin custom_audit_logger
Captures task outcomes and writes structured JSON records to /tmp/ansible_callback_audit.jsonl.
"""

from ansible.plugins.callback import CallbackBase
import time
import json
import os

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'custom_audit_logger'
    CALLBACK_NEEDS_ENABLED = True

    def __init__(self, display=None):
        super(CallbackModule, self).__init__(display)
        self.log_file = "/tmp/ansible_callback_audit.jsonl"
        self._task_start_times = {}

        # Ensure directory exists and log file is fresh
        log_dir = os.path.dirname(self.log_file)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

    def _write_record(self, event_type, payload):
        entry = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "event": event_type,
            "data": payload
        }
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")

    def v2_playbook_on_task_start(self, task, is_conditional):
        self._task_start_times[task._uuid] = time.time()

    def v2_runner_on_ok(self, result):
        duration = 0.0
        start = self._task_start_times.get(result._task._uuid)
        if start:
            duration = round(time.time() - start, 3)

        self._write_record("TASK_COMPLETED", {
            "task_name": result.task_name,
            "host": result._host.name,
            "status": "OK",
            "changed": result._result.get("changed", False),
            "duration_seconds": duration
        })

    def v2_runner_on_failed(self, result, ignore_errors=False):
        duration = 0.0
        start = self._task_start_times.get(result._task._uuid)
        if start:
            duration = round(time.time() - start, 3)

        self._write_record("TASK_FAILED", {
            "task_name": result.task_name,
            "host": result._host.name,
            "status": "FAILED",
            "ignored": ignore_errors,
            "duration_seconds": duration,
            "error_msg": result._result.get("msg", "Unknown error")
        })

    def v2_playbook_on_stats(self, stats):
        recap = {}
        for host in stats.processed:
            recap[host] = stats.summarize(host)

        self._write_record("PLAYBOOK_FINISHED", {
            "recap": recap
        })

