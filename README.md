# OneRecon
OneRecon is a lightweight, beginner-friendly command-line reconnaissance tool built in Python for gathering essential information about target domains. It combines multiple recon steps into a single interface — making it fast and easy to collect WHOIS data, DNS records, ping responses, and subdomains (via crt.sh).

⚙️ Developed by Humza Anwar Khan

🔍 Features

✅ WHOIS Lookup

✅ DNS Lookup (NSLOOKUP)

✅ Ping Test

✅ Subdomain Enumeration (using crt.sh)

✅ Output saved in structured text files

✅ CLI Menu-Based Selection

✅ Fully offline (except for HTTP-based checks)

✅ Easy to modify and extend

🚀 Installation

1. Clone the repository:

```git clone https://github.com/your-username/OneRecon.git``` 
```cd OneRecon```
   
2. Ensure dependencies are installed:

You must have these tools installed on your system:

- whois
- nslookup (part of dnsutils on Linux)
- ping (usually pre-installed)
- subfinder (optional, for subdomain enumeration)

How to use?

Make sure you have Python 3.6+ and the following packages:

`pip install requests python-whois`

🧪 Usage

`python onerecon.py <domain>`

You'll be prompted to select recon steps like:

Select which recon steps to run:
1. WHOIS
2. NSLOOKUP
3. PING
4. SUBFINDER (crt.sh)
Enter options separated by commas (e.g., 1,3,4): 

NOTE: Create a folder with name 'output' , your output will be saved there...


⚠️ Notes

- nslookup and ping must be available on your system (usually pre-installed).
- This tool uses crt.sh (certificate transparency logs) for subdomain enumeration — no API key needed.
- Ensure a working internet connection for network-based checks.


⚙️ How to Contribute


-Feel free to open issues or submit pull requests to:

-Add new reconnaissance commands

-Improve existing functionality

-Enhance output formatting

-Add error handling or dependency checks


# ---Developed by Humza Anwar Khan--- 
