import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

class WebCrawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited_urls = set()
        self.discovered_urls = set()

    def crawl(self):
        self._crawl_url(self.base_url)

    def _crawl_url(self, url):
        if url in self.visited_urls:
            return
        try:
            response = requests.get(url)
            if response.status_code == 200:
                self.visited_urls.add(url)
                self._extract_urls(response.text)
                self._test_endpoint_for_xss(url)
        except Exception as e:
            print(f"Failed to crawl {url}: {e}")

    def _extract_urls(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('http'):
                self.discovered_urls.add(href)
            else:
                full_url = urljoin(self.base_url, href)
                self.discovered_urls.add(full_url)

    def _test_endpoint_for_xss(self, endpoint):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        try:
            driver.get(endpoint)
            payload = "<script>alert('XSS')</script>"
            driver.execute_script(payload)
            alert = Alert(driver)
            if alert.text == "XSS":
                print(f"XSS Vulnerability found at endpoint: {endpoint}")
        except Exception as e:
            print(f"Error testing {endpoint} for XSS: {e}")
        finally:
            driver.quit()

    def get_discovered_urls(self):
        return self.discovered_urls

def display_animation():
    print("Welcome to Cross Crawler - XSS Vulnerability Detection Tool\n")
    print("Author: meownster\n")
    animation = "|/-\\"
    idx = 0
    while True:
        print(f"\rCrawling and testing for XSS vulnerabilities {animation[idx % len(animation)]}", end="")
        idx += 1
        time.sleep(0.1)

def main():
    parser = argparse.ArgumentParser(description="Cross Crawler - XSS Vulnerability Detection Tool")
    parser.add_argument("url", type=str, help="URL of the website to crawl and test for XSS vulnerabilities")
    args = parser.parse_args()

    display_animation()

    crawler = WebCrawler(args.url)
    crawler.crawl()

if __name__ == "__main__":
    main()
