# OneRecon
OneRecon is a simple yet powerful CLI tool written in C for performing essential WEB domain reconnaissance tasks in one place.It automates commands like whois, nslookup, and ping to quickly gather information about target domains and save the results.

🚀 Features

1. Runs WHOIS, NSLOOKUP, and PING tests automatically
2. Saves output neatly into the output/ folder
3. Easy to extend with more recon tools
4. Lightweight and fast, written in pure C

file:///home/humza/Pictures/Screenshots/Screenshot%20from%202025-06-08%2015-40-11.png
![Screenshot from 2025-06-08 15-42-11](https://github.com/user-attachments/assets/95a0734c-8124-41c6-91cf-735220818f20)
![Screenshot from 2025-06-08 15-42-20](https://github.com/user-attachments/assets/52c85ca6-eb87-427c-bf6e-efb9cfa61846)



📥 How to Download and Use

1. Clone the repository:

```git clone https://github.com/your-username/OneRecon.git``` 
```cd OneRecon```
   
2. Ensure dependencies are installed:

You must have these tools installed on your system:

- whois
- nslookup (part of dnsutils on Linux)
- ping (usually pre-installed)
- subfinder (optional, for subdomain enumeration)

NOTE: See the README.md for installation commands.

3. Build the project:

```make```

4. Run the tool:
 
```./OneRecon targetdomain.com```
   
5. View results:

 Check the 'output/' directory for the saved text files with recon data.

⚙️ How to Contribute


-Feel free to open issues or submit pull requests to:

-Add new reconnaissance commands

-Improve existing functionality

-Enhance output formatting

-Add error handling or dependency checks



# ---Developed by Humza Anwar Khan--- 
