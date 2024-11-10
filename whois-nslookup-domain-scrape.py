"""
This script performs WHOIS lookup, NSLookup, and homepage scraping for a given domain.
It saves the WHOIS and NSLookup results to text files and prints the homepage title and description.
"""

import subprocess
import requests
from bs4 import BeautifulSoup
from colorama import Fore, init
import os

init()

EXPORT_DIR = "exported_results"

if not os.path.exists(EXPORT_DIR):
    os.makedirs(EXPORT_DIR)

def whois_lookup(domain):
    try:
        result = subprocess.run(['whois', domain], capture_output=True, text=True, check=True)
        with open(os.path.join(EXPORT_DIR, f"{domain}-whois.txt"), "w") as file:
            file.write(result.stdout)
    except subprocess.CalledProcessError:
        print(Fore.RED + f"Failed to perform WHOIS lookup for {domain}")
    except FileNotFoundError:
        print(Fore.RED + f"WHOIS command not found for {domain}")
    
def nslookup(domain):
    try:
        result = subprocess.run(['nslookup', domain], capture_output=True, text=True, check=True)
        with open(os.path.join(EXPORT_DIR, f"{domain}-nslookup.txt"), "w") as file:
            file.write(result.stdout)
    except subprocess.CalledProcessError:
        print(Fore.RED + f"Failed to perform NSLookup for {domain}")
    except FileNotFoundError:
        print(Fore.RED + f"NSLookup command not found for {domain}")
    except Exception as e:
        print(Fore.RED + f"Error performing NSLookup: {e}")

def scrape_homepage(domain):
    try:
        url = f"http://{domain}"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        description = meta_desc['content'] if meta_desc else "No description found"
        
        report = f"# {domain}\n\n## Title\n{title}\n\n## Description\n{description}"
        print(Fore.GREEN + report)
        
        with open(os.path.join(EXPORT_DIR, f"{domain}.md"), "w") as file:
            file.write(report)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error fetching the homepage: {e}")

def save_summary(domain):
    try:
        with open(os.path.join(EXPORT_DIR, f"{domain}-whois.txt"), "r") as whois_file:
            whois_data = whois_file.read()
        
        with open(os.path.join(EXPORT_DIR, f"{domain}-nslookup.txt"), "r") as nslookup_file:
            nslookup_data = nslookup_file.read()
        
        summary = f"# {domain} Summary\n\n## WHOIS Data\n```\n{whois_data}\n```\n\n## NSLookup Data\n```\n{nslookup_data}\n```"
        
        with open(os.path.join(EXPORT_DIR, f"{domain}-summary.md"), "w") as summary_file:
            summary_file.write(summary)
        
        print(Fore.GREEN + f"Summary saved for {domain}")
    except FileNotFoundError as e:
        print(Fore.RED + f"Error creating summary: {e}")

def main_menu():
    while True:
        print(Fore.CYAN + "1. Whois and NSLookup")
        print(Fore.CYAN + "2. Scrape Homepage and Save Summary")
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
            save_summary(domain)
        elif choice == '3':
            print(Fore.RED + "Exiting...")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
