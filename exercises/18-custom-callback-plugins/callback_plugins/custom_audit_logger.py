#!/usr/bin/python
"""
Starter Custom Callback Plugin: custom_audit_logger
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
        # TODO: Initialize tracking structures

    # TODO: Implement v2_runner_on_ok, v2_runner_on_failed, v2_playbook_on_stats

