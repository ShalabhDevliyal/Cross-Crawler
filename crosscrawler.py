import subprocess
from bs4 import BeautifulSoup
import requests

def fetch_subdomains(domain):
    command = f'sublist3r -d {domain}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    subdomains = result.stdout.splitlines()
    return subdomains

def crawl_for_xss(subdomains):
    xss_vulnerable_urls = []
    for subdomain in subdomains:
        url = f'http://{subdomain}'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # Example: Check if any form inputs are vulnerable to XSS
                forms = soup.find_all('form')
                for form in forms:
                    inputs = form.find_all('input')
                    for input_tag in inputs:
                        if input_tag.get('type') == 'text':
                            xss_vulnerable_urls.append(url)
                            break  # Once a vulnerable input is found, no need to check further
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {url}: {e}")
    
    return xss_vulnerable_urls

def print_cross_crawler_logo():
    logo = r"""
        _____ _ _                 _     _____           _       
       / ____| (_)               | |   / ____|         (_)      
      | |  __| |_ _ __ ___  _ __ | |_ | |     ___  _ __ _  __ _ 
      | | |_ | | | '__/ _ \| '_ \| __|| |    / _ \| '__| |/ _` |
      | |__| | | | | | (_) | | | | |_ | |___| (_) | |  | | (_| |
       \_____|_|_|_|  \___/|_| |_|\__| \_____\___/|_|  |_|\__,_|
                                                                
                                                                
    """
    print(logo)

def main():
    print_cross_crawler_logo()
    print("Welcome to Cross Crawler - Your XSS Vulnerability Scanner!")
    creator = "meownster"
    print(f"Created by {creator} | GitHub: https://github.com/ShalabhDevliyal")
    domain = input("Enter the target domain: ")
    subdomains = fetch_subdomains(domain)
    xss_vulnerable_urls = crawl_for_xss(subdomains)
    
    print("XSS Vulnerable URLs:")
    for url in xss_vulnerable_urls:
        print(url)

if __name__ == "__main__":
    main()
