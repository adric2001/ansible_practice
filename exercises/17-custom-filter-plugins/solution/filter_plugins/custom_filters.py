#!/usr/bin/python
"""
Reference Solution: Custom Jinja2 Filters for Ansible
Provides bytes_to_human, mask_secret, and split_and_trim filters.
"""

class FilterModule(object):
    def filters(self):
        return {
            'bytes_to_human': self.bytes_to_human,
            'mask_secret': self.mask_secret,
            'split_and_trim': self.split_and_trim
        }

    def bytes_to_human(self, bytes_val, unit='auto'):
        """Converts raw byte integer into human-readable string (KB, MB, GB, TB)."""
        try:
            bytes_val = float(bytes_val)
        except (ValueError, TypeError):
            return str(bytes_val)

        units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        if unit != 'auto':
            target_unit = unit.upper()
            if target_unit in units:
                power = units.index(target_unit)
                val = bytes_val / (1024 ** power)
                return f"{val:.2f} {target_unit}"

        for u in units:
            if abs(bytes_val) < 1024.0:
                return f"{bytes_val:.2f} {u}"
            bytes_val /= 1024.0
        return f"{bytes_val:.2f} PB"

    def mask_secret(self, secret_val, show_last=4, mask_char='*'):
        """Masks sensitive strings, revealing only the trailing N characters."""
        if not secret_val:
            return ""
        s = str(secret_val)
        if len(s) <= show_last:
            return mask_char * len(s)
        mask_count = len(s) - show_last
        return (mask_char * mask_count) + s[-show_last:]

    def split_and_trim(self, string_val, delimiter=','):
        """Splits delimited string, strips whitespace, and removes empty items."""
        if not string_val:
            return []
        parts = str(string_val).split(delimiter)
        return [p.strip() for p in parts if p.strip()]
