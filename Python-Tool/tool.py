import socket        # Built-in tool to handle basic internet and IP address lookups
import subprocess    # Built-in tool to run native Windows commands like ping and nslookup
import platform      # Built-in tool to check if your computer is running Windows, Mac, or Linux

# ==========================================
# STEP 1: GET USER INPUT
# ==========================================
# Asks the user to type a website name, removes extra spaces, and saves it in a variable
target_domain = input("Enter domain name to analyze (e.g., google.com): ").strip()

# Prints a clean divider line on the screen to show where the results start
print(f"\n================ Running Complete Diagnostics on: {target_domain} ================")

# ==========================================
# STEP 2: WEBSITE AVAILABILITY CHECKER (PING TEST)
# ==========================================
print("Checking Website Availability...")  # Prints a status message to let the user know what is happening

try:  # Tells Python to try running the code inside this block safely
    # Chooses '-n' for Windows computers or '-c' for Mac/Linux to send 1 connection test packet
    param = "-n" if platform.system().lower() == "windows" else "-c"
    
    # Runs the actual system 'ping' command in the background without showing raw messy text
    response = subprocess.run(["ping", param, "1", target_domain], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if response.returncode == 0:  # If the system command finishes with a success code of 0
        print("Website Status: ONLINE")  # Prints that the website is online and working
    else:  # If the system command returns any code other than 0
        print("Website Status: OFFLINE or Unreachable")  # Prints that the website cannot be reached
except Exception as e:  # Catches any unexpected code errors so the program does not crash
    print(f"Ping failed: {e}")  # Prints the specific error message cleanly on the screen

# ==========================================
# STEP 3: RE-SOLVING PRIMARY IP (SOCKET METHOD)
# ==========================================
print("\n[+] Resolving Primary IP Address...")  # Prints a sub-heading for the IP address lookup step

try:  # Starts an error handling block for the socket lookup
    ip_address = socket.gethostbyname(target_domain)  # Finds the main numeric IPv4 address of the website
    print(f" -> Primary IPv4 Address: {ip_address}")  # Prints the found IP address on the screen
except Exception as e:  # Catches the error if the website name is completely invalid
    print(f" -> Resolution failed: {e}")  # Prints a clean error message instead of crashing

# ==========================================
# STEP 4: ADVANCED DNS RECORDS EXTRACTION (NATIVE NSLOOKUP METHOD)
# ==========================================
# Creates a list of the specific server records we want to search for
record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT']

print("\n[+] Fetching Advanced DNS Server Records...\n")  # Prints a sub-heading for the advanced records section

for record in record_types:  # Starts a loop to go through each record in our list one by one
    print(f"--- {record} Records ---")  # Prints a header showing which record type is currently processing
    try:  # Starts a safe error handling block for the system command lookup
        # Sets up the native Windows 'nslookup' command to look for the specific record type
        cmd = ["nslookup", f"-type={record}", target_domain]
        
        # Executes the nslookup command and captures the output text into a variable
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # Splits the giant block of output text into individual lines so we can read it line by line
        lines = result.stdout.splitlines()
        found_data = False  # Sets up a tracking variable to remember if we found any actual data records
        
        for line in lines:  # Loops through every single line of text returned by the system command
            if "Server:" in line or "Address:" in line:  # Checks if the line contains local computer router info
                if lines.index(line) < 4:  # If it is one of the first few setup lines of the text
                    continue  # Skips this line completely because it is not relevant to the website
            if line.strip() and not line.startswith("Non-authoritative answer:"):  # Skips empty lines and header warnings
                print(f" -> {line.strip()}")  # Prints the actual website record data cleanly on the screen
                found_data = True  # Changes our tracker to True because we successfully displayed a record
                
        if not found_data:  # If the loop finished and our tracker is still False
            print(f" -> No {record} records found or visible via native lookup.")  # Tells the user this folder is empty
            
    except Exception as e:  # Catches network dropouts or command issues safely
        print(f" -> Could not fetch {record} records: {e}")  # Prints a clean failure message on the screen
