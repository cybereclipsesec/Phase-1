# System Information & Environmental Diagnostic Tool

## 🎯 Objective
The main goal of this tool is to make host reconnaissance simple and fast. It automates environment auditing by instantly collecting active user privileges, directory contexts, storage layout maps, and kernel configuration data in a single run without needing any complex technical setups or manual checks.

## 🚀 Features
* **Help Flag Validation:** Automatically validates user input flags and outputs clear usage instructions using the `-h` switch.
* **Analyst Profile Capture:** Interactively captures and verifies the identity name of the active analyst running the sweep.
* **Storage Capacity Mapping:** Sweeps total disk limits and active system mounts via `df -h` to track background memory blocks.
* **OS Telemetry Extraction:** Pulls exact operating system platform build properties and telemetry data using the `uname -a` utility.
* **Instant Error Trapping:** Implements strict validation to instantly halt execution if an unrecognized flag (like `--h`) is typed.
* **Privilege Context Mapping:** Runs security sweeps via `whoami` to verify the exact privilege layer running the script.
* **Network Hostname Query:** Connects with core machine configuration parameters to extract the unique system network hostname.
* **Chronological Timestamping:** Records a definitive calendar date and time marker via the `date` utility for precise audit logging.
* **Absolute Path Context:** Prints the exact storage directory path via `pwd` to show exactly where the tool is executing.

## 🛠️ Prerequisites
* **Operating System:** Linux / Unix-based distributions.
* **Shell Environment:** Native Bash shell (`/bin/bash`).
* **Access Rights:** Standard user permissions (elevated read access may be needed for specific hardware arrays).

## 💻 How to Run
Grant executable permissions to the script and run it inside your terminal:
```bash
chmod +x sysinfo.sh
./sysinfo.sh
```

## 🔍 Example Usage
To print the operational help manual and flag configurations:
```bash
./sysinfo.sh -h
```
To execute the complete system information diagnostic scan:
```bash
./sysinfo.sh
```

## 📋 Example Output
```text
==================================================
  SYSINFO.SH DIAGNOSTIC COMPLIANCE REPORT
==================================================
Execution Timestamp : Tue Oct 20 13:46:12 PKT 2026
Active Project Path : /home/fiza/workspace/bash_tools

[+] Enter Analyst Name: Fiza
[+] Identity Logged  : Analyst Fiza verified.
[+] Privilege Check  : User is running as [fiza]
[+] System Hostname  : secure-node-01

[+] Kernel OS Telemetry:
Linux secure-node-01 5.15.0-88-generic #98-Ubuntu SMP x86_64 GNU/Linux

[+] File System & Disk Capacity Maps:
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        49G   22G   25G  47% /
==================================================
```

## 🚧 Challenges Faced
* **Permission Constraints:** Encountered security blocks where the script could not run until execution rights were explicitly configured via `chmod +x`.
* **Platform Inconsistencies:** Resolved variations in system data formatting across different terminal distributions without causing code syntax breaks.
* **Directory Structural Errors:** Managed folder mapping parameters directly inside the remote version control interface during deployment tracking.

## 🔮 Future Improvements
* **Automated Log Exports:** Build an export module to append terminal outputs directly into a local, timestamped text log file automatically.
* **Defensive Error Traps:** Integrate specialized variable traps to gracefully bypass unprivileged permission alerts without stopping execution.
* **Cross-Platform Support:** Re-engineer core functions to seamlessly recognize and run diagnostics across macOS environments alongside standard Linux.
