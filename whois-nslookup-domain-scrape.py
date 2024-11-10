import os
import subprocess
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

init(autoreset=True)

def whois_lookup(domain):
    result = subprocess.run(['whois', domain], capture_output=True, text=True)
    with open(f"{domain}-whois.txt", "w") as file:
        file.write(result.stdout)

def nslookup(domain):
    result = subprocess.run(['nslookup', domain], capture_output=True, text=True)
    with open(f"{domain}-nslookup.txt", "w") as file:
        file.write(result.stdout)

def scrape_homepage(domain):
    url = f"http://{domain}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string if soup.title else "No title found"
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    description = meta_desc['content'] if meta_desc else "No description found"
    
    report = f"Title: {title}\nDescription: {description}"
    print(Fore.GREEN + report)

def main_menu():
    while True:
        print(Fore.CYAN + "1. Whois and NSLookup")
        print(Fore.CYAN + "2. Scrape Homepage")
        print(Fore.CYAN + "3. Exit")
        choice = input(Fore.YELLOW + "Enter your choice: ")

        if choice == '1':
            domain = input(Fore.YELLOW + "Enter domain: ")
            whois_lookup(domain)
            nslookup(domain)
            print(Fore.GREEN + f"Whois and NSLookup results saved for {domain}")
        elif choice == '2':
            domain = input(Fore.YELLOW + "Enter domain: ")
            scrape_homepage(domain)
        elif choice == '3':
            print(Fore.RED + "Exiting...")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()