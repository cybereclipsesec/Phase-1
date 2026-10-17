#!/bin/bash

# Check if the user passed the '-h' argument for help 
if [ "$1" == "-h" ]; then
     # Display clear usage instructions to the analyst
     echo "Usage: ./sysinfo.sh"
    # Exit safely with status code 0 (success)
     exit 0
# Check if the user passed any other invalid argument
elif [ "$1" != "" ]; then
     # Display an error message explaining how to get help
     echo "Error: Invalid argument. Use -h for help"
     # Exit with status code 1 indicating a user input error
     exit 1
fi

# Request the active analyst's name to personalize the output header
echo "Enter your name:"
# Capture and save the typed input text into a variable name  'name'
read name

# Print a friendly interactive greeting banner using the input variable
echo "Hello $name! here is your system's info"
echo "......................................."
# Pause the execution for 1 second
sleep 1
echo "Loading....."
sleep 1
echo "================================="
echo "       System Information        "
echo "================================="

# Display the name of the logged-in user running this security sweep
echo "Current user: "
whoami
sleep 1

# Extract and display the specific machine network node name
echo "Computer name: "
hostname
sleep 1

# Print the  absolute directory path where this script is running 
echo "Current Directory: "
pwd
sleep 1

# Record a definitive date and time stamp for auditing logs
echo "Date & Time: "
date
sleep 1

# Provide a comprehensive human-readable map of disk storage blocks
echo "Disk Space: "
df -h
sleep 1

# Query the Linux kernel and distribution hardware properties
echo "System info: "
uname -a
echo "......................................."

