# Exercise 20: Security Hardening & CIS Compliance Automation

## 🎯 Objective
Design an advanced production server hardening and compliance audit playbook applying Center for Internet Security (CIS) benchmark principles to secure SSH configuration, kernel sysctl parameters, and access permissions.

## 📖 Key Concepts

### 1. Hardening Surface Areas
- **SSH Daemon (`/etc/ssh/sshd_config`)**:
  - `PermitRootLogin no`: Disallow direct root SSH access.
  - `PasswordAuthentication no`: Enforce SSH key-based authentication.
  - `X11Forwarding no`: Prevent display hijacking.
  - `ClientAliveInterval 300` / `ClientAliveCountMax 0`: Auto-disconnect idle sessions after 5 minutes.
  - `MaxAuthTries 3`: Mitigate brute-force login attacks.
- **Kernel Parameter Hardening (`/etc/sysctl.d/99-security.conf`)**:
  - `net.ipv4.ip_forward = 0`: Prevent hosts from acting as network routers.
  - `net.ipv4.conf.all.send_redirects = 0`: Disable ICMP redirect broadcasts.
  - `net.ipv4.tcp_syncookies = 1`: Protect against SYN flood attacks.
  - `fs.suid_dumpable = 0`: Prevent core dumps of setuid programs containing memory secrets.
- **Auditing & Compliance Verification**:
  - Running playbooks in check mode (`--check --diff`) produces non-destructive compliance audit reports.

---

## 🏢 The Scenario
You are the Security Lead at a financial institution. You need to automate host security hardening targeting `/tmp/compliance_lab/`:
1. Deploy hardened `/tmp/compliance_lab/sshd_config` with validation.
2. Deploy hardened `/tmp/compliance_lab/99-security-sysctl.conf`.
3. Audit file system permissions: ensure `/tmp/compliance_lab/secure_keys/` has mode `0700`.
4. Implement an audit compliance assertion task validating all hardening rules in check mode!

---

## 📝 Tasks
1. Complete `playbook.yml`.
2. Execute against localhost.
3. Run with `--check --diff` to verify compliance reporting.

---

## 🔍 Verification Commands

```bash
# Execute hardening playbook
ansible-playbook -i "localhost," -c local playbook.yml

# Verify in check mode
ansible-playbook -i "localhost," -c local playbook.yml --check --diff
```

