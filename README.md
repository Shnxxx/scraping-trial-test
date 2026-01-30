# Business Registry Web Scraper

## Overview

This project is a Python web scraper that extracts business registry records from a demo website:

https://scraping-trial-test.vercel.app

The website includes:
- Dynamic (client-side) rendering (React / Next.js)
- Pagination
- Google reCAPTCHA

Because of these constraints, Selenium is used to simulate real user behavior and reliably extract data.

The script:
- Accepts a user-provided search term
- Navigates through all result pages
- Opens each business profile
- Extracts detailed business and registered agent information
- Saves results to both JSON and CSV formats

---

## Table of Contents

- [Overview](#overview)
- [What Data Is Extracted](#what-data-is-extracted)
- [Output Files](#output-files)
- [Requirements](#requirements)
- [Version Information](#version-information)
- [Step-by-Step Installation (Beginner Friendly)](#step-by-step-installation-beginner-friendly)
- [How to Run the Script](#how-to-run-the-script)
- [Search Term Rules](#search-term-rules)
- [Pagination Handling](#pagination-handling)
- [Error Handling & Logging](#error-handling--logging)
- [Performance Notes](#performance-notes)
- [Limitations](#limitations)
- [Repository Structure](#repository-structure)
- [Versioning](#versioning)
- [Authors-notes](#authors-notes)
- [Author](#author)

---

## What Data Is Extracted

For each business, the scraper extracts the following fields from the **Business Profile** page:

- Business Name
- Registration ID
- Status
- Filing Date
- Registered Agent Name
- Registered Agent Address
- Registered Agent Email (if available)

No fields are guessed or fabricated. All data is scraped directly from the site.

---

## Output Files

After execution, two output files are created in the project directory.

### output.json (example)

```json
{
  "business_name": "Silver Tech CORP",
  "registration_id": "SD0000001",
  "status": "Active",
  "filing_date": "1999-12-04",
  "agent_name": "Sara Smith",
  "agent_address": "1545 Maple Ave",
  "agent_email": "sara.smith@example.com"
}
```

### output.csv (example)

| business_name     | registration_id | status | filing_date | agent_name | agent_address  | agent_email              |
|-------------------|-----------------|--------|-------------|------------|----------------|--------------------------|
| Silver Tech CORP  | SD0000001       | Active | 1999-12-04  | Sara Smith | 1545 Maple Ave | sara.smith@example.com   |

Each row represents one business entity.

---

## Requirements

Before running the script, ensure you have:

- A computer (Windows, macOS, or Linux)
- Internet connection
- Python 3.x
- Mozilla Firefox browser
- GeckoDriver (Firefox WebDriver)
- Git (optional, for cloning)

---

### GeckoDriver Requirement (Important)

This project uses Selenium with Mozilla Firefox.

You must have **geckodriver** installed and available in your system PATH.

Download GeckoDriver from:
https://github.com/mozilla/geckodriver/releases

After installation, ensure that running the following command works in your terminal:

```
geckodriver --version
```

---

## Version Information

This repository uses **Semantic Versioning**.

The latest stable release is:

**v1.3.0**

This version includes:
- Full business profile scraping
- Registered agent extraction
- JSON and CSV output
- Pagination stability improvements
- Performance optimizations

---

## Step-by-Step Installation (Beginner Friendly)

### Option A: Download the Stable Version (No Git Required)

1. Open your browser
2. Go to: https://github.com/Shnxxx/scraping-trial-test
3. Click **Tags**
4. Select **v1.3.0**
5. Click **Code → Download ZIP**
6. Extract the ZIP file
7. Open a terminal **inside the extracted folder**

---

### Option B: Clone Using Git

Open a terminal or command prompt and type:

```bash
git clone https://github.com/Shnxxx/scraping-trial-test.git
cd scraping-trial-test
git checkout v1.3.0
```

---

### (Optional but Recommended) Create a Virtual Environment

In the terminal, inside the project folder, type:

```bash
python -m venv .venv
```

Activate it:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

---

### Install Required Python Library

```bash
pip install selenium
```

---

## How to Run the Script

In the terminal (inside the project folder):

```bash
python scraper.py
```

### What Happens Next

1. Firefox opens automatically
2. A CAPTCHA appears
3. Solve the CAPTCHA manually
4. Return to the terminal and press ENTER
5. Enter a search term (minimum 3 characters)
   - Press ENTER to use the default `LLC`
6. The script navigates all pages and business profiles
7. Results are saved to:
   - `output.json`
   - `output.csv`

---

## Search Term Rules

- Minimum of **3 characters**
- Empty searches are not allowed
- Wildcard searches are not supported

Default:
```
LLC
```

Examples:
```
Tech
Silver TECH
```

---

## Pagination Handling

- The site displays results across multiple pages (e.g., “Page 1 of 25”)
- The script detects page changes using stable UI text
- All pages are processed automatically

---

## Error Handling & Logging

- Explicit waits handle dynamic content loading
- Optional fields (e.g., agent email) are handled safely
- Errors are logged to:
```
scraper.log
```
- A failed business does not stop the script

---

## Performance Notes

- Each business profile opens in a temporary browser tab
- Tabs are closed immediately after scraping
- A short delay is added to avoid CAPTCHA re-triggering
- Large searches (e.g., 500 businesses) may take several minutes

This is expected for browser-based scraping.

---

## Limitations

- CAPTCHA must be solved manually
- Resume-after-crash is not implemented
- Browser automation is slower than direct APIs
- Full registry enumeration without a search term is not possible

---

## Repository Structure

```
scraping-trial-test/
├── scraper.py
├── output.json
├── output.csv
├── scraper.log
├── README.md
├── .gitignore
```

---

## Versioning

- v1.0.0 – Initial working scraper
- v1.1.0 – Business profile navigation
- v1.2.0 – CSV output and stability fixes
- v1.3.0 – Agent scraping, performance tuning, documentation polish

The `main` branch always reflects the latest stable release.

---

## Author’s Notes

This solution was implemented with an emphasis on correctness, clarity, and respect for the constraints imposed by the target website.

### Choice of Selenium
The site uses dynamic rendering, client-side pagination, and reCAPTCHA. A traditional requests + BeautifulSoup approach would not reliably capture rendered content or user interactions.

### CAPTCHA Behavior
After the initial CAPTCHA is solved, the browser session remains valid for a limited time. The script relies on this behavior and does not attempt to bypass CAPTCHA protections.

### Pagination Strategy
Directly waiting on table rows caused stale element errors due to React re-renders. Stable page indicators were used instead.

### Resume Capability
Persistent resume logic was intentionally not implemented. CAPTCHA-protected browser sessions make durable resume behavior complex and out of scope.

### Search Scope
The site enforces a minimum search length and disallows wildcard searches. The scraper operates strictly within those constraints.

Overall, the goal is a clean, transparent, and responsible scraper that reflects real-world constraints.

---

## Author

Senjo  
GitHub: https://github.com/Shnxxx
