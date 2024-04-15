# Cross Crawler

Cross Crawler is a Python-based tool designed to help bug bounty hunters and security researchers identify XSS (Cross-Site Scripting) vulnerabilities in websites. It automates the process of discovering active subdomains associated with a target domain and then crawls each subdomain to detect potential XSS vulnerabilities.


# Cross Crawler - XSS Vulnerability Detection Tool

Cross Crawler is a command-line tool for detecting XSS (Cross-Site Scripting) vulnerabilities in web applications. It crawls through a given website, extracts URLs, and tests each endpoint for potential XSS vulnerabilities.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/CrossCrawler.git
    ```

2. Navigate to the project directory:
    ```bash
    cd CrossCrawler
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the tool by executing the `crawler.py` script and providing the URL of the website you want to test:

```bash
python crawler.py <website_url>
```

## Workflow

Crawling Phase: The tool starts by crawling the specified website. It extracts all the URLs found in the web pages of the website.

Testing Phase: After crawling, the tool tests each discovered endpoint for potential XSS vulnerabilities. It injects a simple XSS payload into the endpoint and checks for any execution of malicious scripts.

Example

```bash
python crawler.py https://example.com

```

This command will start the Cross Crawler tool and test the website at https://example.com for XSS vulnerabilities.
