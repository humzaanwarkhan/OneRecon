import os
import socket
import subprocess
import whois
import requests

def create_output_dir():
    if not os.path.exists("output"):
        os.makedirs("output")
        print("[+] Created 'output' directory.\n")

def run_whois(domain):
    print("[*] Running WHOIS...")
    try:
        info = whois.whois(domain)
        with open("output/whois.txt", "w") as f:
            f.write(str(info))
        print("[+] WHOIS info saved to output/whois.txt\n")
    except Exception as e:
        print(f"[-] WHOIS failed: {e}\n")

def run_nslookup(domain):
    print("[*] Running NSLOOKUP...")
    try:
        result = subprocess.check_output(["nslookup", domain], stderr=subprocess.STDOUT, text=True)
        with open("output/nslookup.txt", "w") as f:
            f.write(result)
        print("[+] NSLOOKUP result saved to output/nslookup.txt\n")
    except Exception as e:
        print(f"[-] NSLOOKUP failed: {e}\n")

def run_ping(domain):
    print("[*] Running PING...")
    try:
        result = subprocess.check_output(["ping", "-c", "4", domain], stderr=subprocess.STDOUT, text=True)
        with open("output/ping.txt", "w") as f:
            f.write(result)
        print("[+] Ping result saved to output/ping.txt\n")
    except Exception as e:
        print(f"[-] Ping failed: {e}\n")

def run_subfinder(domain):
    print("[*] Finding subdomains using crt.sh...")
    try:
        url = f"https://crt.sh/?q=%.{domain}&output=json"
        r = requests.get(url, timeout=10)
        subdomains = set()
        if r.status_code == 200:
            for entry in r.json():
                name = entry['name_value']
                for sub in name.split('\n'):
                    if domain in sub:
                        subdomains.add(sub.strip())

        with open("output/subdomains.txt", "w") as f:
            if subdomains:
                for sd in sorted(subdomains):
                    f.write(sd + "\n")
                print(f"[+] Found {len(subdomains)} subdomains. Saved to output/subdomains.txt\n")
            else:
                f.write("No subdomains found.")
                print("[-] No subdomains found.\n")
    except Exception as e:
        print(f"[-] Subdomain scan failed: {e}\n")

def main():
    import sys
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <domain>")
        return

    domain = sys.argv[1]

    print("""
          

 .88888.                     888888ba                                      
d8'   `8b                    88    `8b                                     
88     88 88d888b. .d8888b. a88aaaa8P' .d8888b. .d8888b. .d8888b. 88d888b. 
88     88 88'  `88 88ooood8  88   `8b. 88ooood8 88'  `"" 88'  `88 88'  `88 
Y8.   .8P 88    88 88.  ...  88     88 88.  ... 88.  ... 88.  .88 88    88 
 `8888P'  dP    dP `88888P'  dP     dP `88888P' `88888P' `88888P' dP    dP 

               
                    -By Humza Anwar Khan                   
                                                                           
""")

    print(f"Target: {domain}\n")

    print("Select which recon steps to run:")
    print("1. WHOIS")
    print("2. NSLOOKUP")
    print("3. PING")
    print("4. SUBFINDER (crt.sh)")
    options = input("Enter options separated by commas (e.g., 1,3,4): ").strip()

    create_output_dir()

    choices = options.split(',')
    for choice in choices:
        choice = choice.strip()
        if choice == '1':
            run_whois(domain)
        elif choice == '2':
            run_nslookup(domain)
        elif choice == '3':
            run_ping(domain)
        elif choice == '4':
            run_subfinder(domain)
        else:
            print(f"[-] Invalid option: {choice}\n")

    print("[+] Recon finished. Output saved in the 'output' directory.\n")

if __name__ == "__main__":
    main()
