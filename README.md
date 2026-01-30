# Business Registry Web Scraper

## Overview

This project is a Python web scraper that extracts business registry records from the following website:

Target URL:  
https://scraping-trial-test.vercel.app

The website uses dynamic rendering, pagination, and CAPTCHA protection.  
For this reason, Selenium was used to ensure correct interaction with the page and reliable data extraction.

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
- [Versioning](#versioning)
- [Author’s Notes](#authors-notes)
- [Author](#author)

---

## Extracted Fields

For each business entity returned by the search results, the scraper extracts:

- Business Name  
- Registration ID / Entity Number  
- Status  
- Filing Date  

### Agent Details (Important Note)

The task description includes agent details (name, address, email) in the example output.  
However, after inspecting the target website:

- Agent information is not present on the search results page  
- No agent fields are exposed without navigating to individual detail pages or undocumented endpoints  

To avoid fabricating or guessing data, agent details are not included in the output.

This limitation is documented intentionally to ensure transparency.


---

## Requirements

- Python 3.x  
- Mozilla Firefox  
- geckodriver (compatible with Firefox)  
- Selenium  

---

## Installation

### 1. Clone the repository

    git clone https://github.com/YOUR_USERNAME/scraping-trial-test.git
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

### Runtime behavior

1. A Firefox browser window opens  
2. The user is prompted to solve the CAPTCHA manually  
3. After solving the CAPTCHA, press ENTER in the terminal  
4. The script performs a search and paginates through all available result pages  
5. Extracted data is saved to output.json  

---

## Search Term Configuration

The website enforces the following constraints:

- A minimum of three characters is required for searching  
- Empty searches, single-character searches, and wildcard searches are not allowed  

By default, the script uses the search term:

    LLC

This search term returns a large dataset and is suitable for demonstrating correct pagination handling.

The script also allows the user to override the default search term at runtime (e.g. "Tech"), provided the input meets the minimum length requirement.

Because the site does not expose a way to list all registered businesses without a search query, full enumeration of the entire registry is not possible and is intentionally not attempted.

---

## Pagination Handling

- The site returns results across multiple pages  
- The scraper automatically navigates through all available pages for the given search term  
- Pagination completion is detected using stable UI state (page indicators), avoiding reliance on volatile DOM elements  

---

## Output

The final output is written to:

    output.json

Each record follows this structure:

    {
      "business_name": "ABC COMPANY LLC",
      "registration_id": "123456",
      "status": "Active",
      "filing_date": "2023-05-14"
    }

---

## Error Handling and Logging

The script includes basic error handling and logging:

- Explicit waits are used to handle dynamic page loading  
- Unexpected HTML structures are handled safely  
- Pagination termination is detected cleanly  
- Errors and important events are logged to:

    scraper.log

---

## Design Decisions

- Selenium was chosen due to dynamic rendering and CAPTCHA protection  
- Manual CAPTCHA solving is required and intentionally documented  
- Pagination logic avoids brittle DOM references and stale element errors  
- The script prioritizes correctness, clarity, and robustness over over-engineering  

---

## Limitations

- CAPTCHA must be solved manually  
- Agent details are not available on the search results page  
- The site does not provide a public method to retrieve all businesses without a search query  
- Full registry enumeration is therefore not possible  

---

## Repository Structure

    .
    ├── scraper.py
    ├── output.json
    ├── scraper.log
    ├── README.md
    ├── .gitignore

Virtual environments and IDE files are intentionally excluded.

---

## Versioning

- The main branch contains the stable solution  
- Releases are tagged using semantic versioning (e.g. v1.0.0)  

---

## Notes

This implementation focuses on:

- Correctness of extracted data  
- Reliable pagination handling  
- Clear and maintainable code  
- Honest documentation of constraints  

---

## Author’s Notes

This solution was implemented with an emphasis on correctness, clarity, and
respect for the constraints imposed by the target website.

### Choice of Selenium
The target site uses dynamic rendering, client-side pagination, and CAPTCHA
protection. Because of this, a traditional requests + BeautifulSoup approach
would not reliably capture the rendered content. Selenium was chosen to ensure
that the scraper interacts with the page in the same way a real user does.

### CAPTCHA Handling
The CAPTCHA was intentionally handled manually. Attempting to bypass or automate
CAPTCHA solving was avoided, as it would be out of scope for this task and could
violate usage expectations. The script pauses execution until the user confirms
that the CAPTCHA has been solved.

### Pagination Strategy
Several pagination approaches were evaluated during development. Directly
waiting on table rows proved unreliable due to DOM re-rendering and stale element
references in a React-based frontend. The final implementation uses stable UI
state (page indicators) to detect page transitions, which resulted in consistent
and complete pagination across all available pages.

### Search Scope Decisions
The website enforces a minimum search length of three characters and does not
support empty or wildcard searches. Because of this, the scraper operates on a
search-term basis rather than attempting full registry enumeration.

The default search term "LLC" was chosen because it returns a sufficiently large
dataset to demonstrate pagination handling. The script allows the user to
override this value (e.g. using "Tech") to support flexibility without guessing
or brute-forcing search terms.

### Agent Details
Although agent details were included in the task’s example output, they are not
available on the search results page. To maintain data integrity, agent fields
were intentionally excluded rather than populated with placeholder or inferred
values.

Overall, the goal of this implementation was to provide a clean, reliable, and
transparent scraper that reflects real-world constraints and responsible data
collection practices.

## Author

Senjo