# Business Registry Web Scraper

## Overview

This project is a Python web scraper that extracts business registry records from the following website:

**Target URL:**  
https://scraping-trial-test.vercel.app

The website uses dynamic rendering, paginated results, and CAPTCHA protection.  
For this reason, **Selenium** was used to ensure correct interaction with the page and reliable data extraction.

---

## Table of Contents

- [Overview](#overview)
- [Extracted Fields](#extracted-fields)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Run the Script](#how-to-run-the-script)
- [Search Term Configuration](#search-term-configuration)
- [Pagination Handling](#pagination-handling)
- [Output](#output)
- [Error Handling and Logging](#error-handling-and-logging)
- [Design Decisions](#design-decisions)
- [Limitations](#limitations)
- [Repository Structure](#repository-structure)
- [Author’s Notes](#authors-notes)
- [Author](#author)

---

## Extracted Fields

For each business entity returned by the search results table, the scraper extracts:

- Business Name  
- Registration ID / Entity Number  
- Status  
- Filing Date  

---

## Requirements

- Python 3.x  
- Mozilla Firefox  
- geckodriver (compatible with Firefox)  
- Selenium  

---

## Installation

### 1. Clone the repository

git clone https://github.com/Shnxxx/scraping-trial-test.git  
cd scraping-trial-test  

### 2. (Optional) Create and activate a virtual environment

python -m venv .venv  
source .venv/bin/activate      # macOS / Linux  
.venv\Scripts\activate         # Windows  

### 3. Install dependencies

pip install selenium  

---

## How to Run the Script

python scraper.py  

### Runtime Behavior

1. A Firefox browser window opens  
2. The user is prompted to solve the CAPTCHA manually  
3. After solving the CAPTCHA, press **ENTER** in the terminal  
4. The script performs a search and paginates through all available result pages  
5. Extracted data is saved to `output.json` and `output.csv`  

---

## Search Term Configuration

The website enforces the following constraints:

- A **minimum of three characters** is required for searching  
- Empty searches, single-character searches, and wildcard searches are not allowed  

By default, the script uses the search term:

LLC  

The user may override this value at runtime (e.g. `Tech`).  
Input is validated and the user is re-prompted until a valid search term is provided.

Because the site does not expose a way to list all registered businesses without a
search query, full registry enumeration is **not possible** and is intentionally
not attempted.

---

## Pagination Handling

- The site returns results across multiple pages  
- The scraper automatically navigates through **all available pages** for the
  given search term  
- Pagination completion is detected using stable UI state (page indicators),
  avoiding reliance on volatile DOM elements  

---

## Output

The final output is written to:

output.json  
output.csv  

### JSON Output (output.json)

Each record represents a single business entity and follows this structure:

{
  "business_name": "ABC COMPANY LLC",
  "registration_id": "123456",
  "status": "Active",
  "filing_date": "2023-05-14"
}

### CSV Output (output.csv)

The CSV file contains the same data, with one record per row:

business_name,registration_id,status,filing_date  
ABC COMPANY LLC,123456,Active,2023-05-14  

### Agent Details (Important Note)

Although agent details (name, address, email) were included in the task’s example
output, the target website’s **search results table does not expose any agent
information**.

Because this data is not available on the page being scraped, agent-related
fields are intentionally **not included** in the output. Generating placeholder
or inferred values for non-existent data was avoided to preserve data accuracy
and integrity.

---

## Error Handling and Logging

The script includes basic error handling and logging:

- Explicit waits handle dynamic page loading and temporary delays  
- Unexpected or missing HTML elements are handled safely  
- Pagination termination is detected cleanly  
- Errors and important events are logged to:

scraper.log  

---

## Design Decisions

- **Selenium** was chosen due to dynamic rendering and CAPTCHA protection  
- Manual CAPTCHA solving is required and intentionally documented  
- Pagination logic avoids brittle DOM references and stale element errors  
- The script prioritizes correctness, clarity, and robustness over
  over-engineering  

---

## Limitations

- CAPTCHA must be solved manually  
- Agent details are not available on the search results page  
- The site does not provide a public method to retrieve all businesses without a
  search query  
- Full registry enumeration is therefore not possible  

---

## Repository Structure

.
├── scraper.py  
├── output.json  
├── output.csv  
├── scraper.log  
├── README.md  
├── .gitignore  

Virtual environments and IDE files are intentionally excluded.

---

## Author’s Notes

This solution was implemented with an emphasis on correctness, clarity, and
respect for the constraints imposed by the target website.

### Choice of Selenium

The target site uses dynamic rendering, client-side pagination, and CAPTCHA
protection. A traditional requests + BeautifulSoup approach would not reliably
capture the rendered content. Selenium was chosen to ensure the scraper interacts
with the page in the same way a real user does.

### CAPTCHA Behavior

After the initial CAPTCHA is solved, the session remains valid for a limited
period of time, allowing continued pagination without repeated challenges.  
This script relies on that session behavior and pauses execution until the user
confirms that the CAPTCHA has been completed. No attempt is made to automate or
bypass CAPTCHA challenges.

### Pagination Strategy

Several pagination approaches were evaluated during development. Directly
waiting on table rows proved unreliable due to DOM re-rendering and stale element
references in a React-based frontend. The final implementation uses stable UI
state (page indicators) to detect page transitions, resulting in consistent and
complete pagination.

### Resume Capability

A persistent resume mechanism (e.g., restarting from the last processed page
after a script or browser restart) was intentionally not implemented.  
Given the use of CAPTCHA-protected browser sessions and the limited scope of this
task, adding persistent state management would increase complexity without clear
benefit.

### Search Scope Decisions

The website enforces a minimum search length of three characters and does not
support empty or wildcard searches. The scraper therefore operates on a
search-term basis rather than attempting full registry enumeration.

The default search term "LLC" was chosen because it returns a sufficiently large
dataset to demonstrate pagination handling. The user may override this value
(e.g. "Tech") to support flexibility without guessing or brute-forcing search
terms.

Overall, the goal of this implementation is to provide a clean, reliable, and
transparent scraper that reflects real-world constraints and responsible data
collection practices.

---

## Author

Senjo
