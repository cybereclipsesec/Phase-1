# Network Diagnostics & Advanced DNS Lookup Tool

## 🎯 Objective
The main goal of this tool is to make network troubleshooting simple and fast. It helps users instantly check if a website is online and automatically gathers advanced background server information (like where its emails or security configuration data are stored) without needing any complex technical setups or third-party software installations.

## 🚀 Features
* **Website Ping Checker:** Automatically tests if a target website is awake, responding, and working properly.
* **IP Address Finder:** Instantly tracks down and displays the main numeric address (IPv4) of any domain name.
* **Deep Server Record Scanner:** Seamlessly loops through the website's background directories to gather technical records (`A`, `AAAA`, `MX`, `NS`, `TXT`).
* **Smart Output Filtering:** Automatically cleans up raw system text, strips away messy warning lines, and hides your personal home router gateway address to keep your setup safe and clean.

## 📋 Requirements
* **Language:** Python 3.10 or higher (Fully optimized and tested on Python 3.15).
* **Libraries Used:** None! This tool only uses Python's built-in factory components (`socket`, `subprocess`, `platform`). You do not need to download or install anything using `pip`.
* **System Environment:** Fully compatible with Windows PowerShell / Command Prompt, macOS, and Linux terminals.

## 💻 How to Run
1. Open your code editor terminal window (or your system Command Prompt/PowerShell).
2. Start the program by typing this exact command and hitting **Enter**:
   ```bash
   python tool.py
   ```
3. Type the website domain name you want to test (for example: `google.com` or `linkedin.com`) when prompted on the screen and press **Enter**.

## 📝 Example Usage
```text
Enter domain name to analyze (e.g., google.com): linkedin.com
```

## 📊 Example Output
```text
================ Running Complete Diagnostics on: linkedin.com ================
Checking Website Availability...
Website Status: ONLINE

[+] Resolving Primary IP Address...
 -> Primary IPv4 Address: 13.107.42.14

[+] Fetching Advanced DNS Server Records...

--- A Records ---
 -> linkedin.com internet address = 13.107.42.14
--- AAAA Records ---
 -> linkedin.com IPv6 address = 2620:1ec:c11::14
--- MX Records ---
 -> linkedin.com mail exchanger = ://outlook.com
--- NS Records ---
 -> linkedin.com nameserver = ://linkedin.com
--- TXT Records ---
 -> linkedin.com text = "v=spf1 include:://linkedin.com ~all"
```

## ⚠️ Challenges Faced
* **Third-Party Package Restrictions:** Originally, the script relied on an external library called `dnspython`. However, the local computer's environment layout completely blocked global installations, throwing "externally managed environment" errors.
  * **The Fix:** I completely modified the structure to use Windows' native background utility (`nslookup`) via Python's built-in sub-processing. This eliminated the need for any terminal installations and made the tool work instantly on any computer out of the box.
* **Messy Output & Security Exposure:** The raw text returned by the system command included long, confusing system header text and accidentally printed my personal home router IP gateway address.
  * **The Fix:** I wrote a custom text filtering loop that identifies local router markers, skips over those lines completely, and cleans up the visual layout so only the target website's records are displayed.

## 🔮 Future Improvements
* **Automated File Exports:** Add a built-in feature that automatically saves the final terminal output into a clean, well-formatted text file or PDF report for submission.
* **Batch Domain Processing:** Allow the user to input a whole list of multiple websites at the same time from a local text document instead of typing them one by one.
* **Physical Location Mapping:** Integrate a free IP geolocation layout feature to show the physical country and city where the website's hosting server is actually located.

