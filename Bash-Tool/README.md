#Scripting and Automation - Phase 1: Bash System Info Tool

##Tool Name
sysinfo.sh (System Information Diagnostic Tool)

##Objectives
Automates host reconnaissance by collecting - active user privileges, directory contexts, storage layout maps, and kernel configuration data in a single run.

##Features
 - Validates user input flags and output usage instructions with the -h switch.
 - Interactively captures the active analyst profile name.
 - Sweeps disk capacity limit and mounts via df -h tracking blocks.
 - Extract OS platform build properties via uname -a telemetry.
 - Traps input errors instantly to stop execution if an unrecognized flag like --h is typed.
 - Maps active user privilege contexts to see who is running the security sweep via whoami.
 - Queries the core machine configuration parameters to extract the unique network hostname.
 - Record a definitive chronological calendar timestamp via the date utility for logging.
 - Prints the absolute directory storage path context via pwd where the tool executes.
 
##How to run
chmod +x tool.sh
./tool.sh

##Screenshots Explanation
The attached screenshots show that code features have proper comments starting with #. The output proof shows the script running perfectly for user Fiza, tracking the exact  execution timestamps and catching input errors smoothly.
