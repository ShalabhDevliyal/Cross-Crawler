# Cross Crawler

Cross Crawler is a Python-based tool designed to help bug bounty hunters and security researchers identify XSS (Cross-Site Scripting) vulnerabilities in websites. It automates the process of discovering active subdomains associated with a target domain and then crawls each subdomain to detect potential XSS vulnerabilities.

## Features

- Fetches active subdomains using Sublist3r
- Crawls each subdomain to identify XSS vulnerable URLs
- Displays a cool CLI terminal graphic with the tool's name upon execution
- Dynamic user input for specifying the target domain
- Created by meownster (@ShalabhDevliyal) - [GitHub Profile](https://github.com/ShalabhDevliyal)

## Installation

1. Clone or download the repository onto your local machine.

2. Install the required Python packages by running the following command in your terminal:



## Usage

1. Open a terminal or command prompt and navigate to the directory where you saved the Python script.

2. Run the script by executing the following command:



3. Enter the target domain for which you want to scan for XSS vulnerabilities when prompted.

4. Wait for the scan to complete. Depending on the size of the domain, the scan may take some time.

5. Review the list of vulnerable URLs displayed by the script to identify potential XSS vulnerabilities in the target domain.

6. If XSS vulnerabilities are found, report them responsibly to the website owner or the appropriate authority.

7. Exit the script by closing the terminal window or pressing Ctrl+C.

## Disclaimer

Use this tool responsibly and only on websites where you have permission to perform security testing. The author takes no responsibility for any misuse of this tool.

## License

This project is licensed under the [MIT License](LICENSE).
