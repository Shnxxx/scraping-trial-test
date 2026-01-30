# Business Registry Web Scraper

## Overview

This project is a Python web scraper that extracts business registry records from a demo website:

https://scraping-trial-test.vercel.app

The website uses:
- Dynamic (client-side) rendering
- Pagination
- Google reCAPTCHA

Because of these constraints, Selenium is used to simulate real user behavior and reliably extract data.

The script:
- Accepts a search term
- Navigates all result pages
- Opens each business profile
- Extracts detailed business and registered agent information
- Saves the results to **JSON** and **CSV**

---

## What Data Is Extracted

For each business, the scraper collects:

- Business Name
- Registration ID
- Status
- Filing Date
- Registered Agent Name
- Registered Agent Address
- Registered Agent Email (if available)

All data comes directly from the **Business Profile** page.

---

## Output Files

After the script finishes, two files are created in the project folder:

### `output.json`
Example:
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

### `output.csv`
Example:

| business_name    | registration_id | status | filing_date | agent_name | agent_address | agent_email |
|------------------|-----------------|--------|-------------|------------|---------------|-------------|
| Silver Tech CORP | SD0000001       | Active | 1999-12-04  | Sara Smith | 1545 Maple Ave | sara.smith@example.com |

Each row represents one business entity.

---

## Requirements

Before running the script, make sure you have:

- A computer (Windows, macOS, or Linux)
- Internet connection
- Mozilla Firefox browser
- Python 3.x installed

No prior programming experience is required to **run** the script.

---

## Step-by-Step Installation (Beginner Friendly)

### Step 1: Install Python

1. Open your web browser
2. Go to: https://www.python.org/downloads/
3. Download **Python 3.x**
4. During installation:
   - ✔ Check **“Add Python to PATH”**
5. Finish installation

To verify:
- Open **Command Prompt** (Windows) or **Terminal** (macOS/Linux)
- Type:
```bash
python --version
```

---

### Step 2: Install Firefox

1. Go to: https://www.mozilla.org/firefox/
2. Download and install Firefox

---

### Step 3: Open a Terminal / Command Prompt

- **Windows**:
  - Press `Windows + R`
  - Type `cmd`
  - Press Enter

- **macOS**:
  - Press `Command + Space`
  - Type `Terminal`
  - Press Enter

- **Linux**:
  - Open your terminal application

All commands below are typed **inside this window**.

---

### Step 4: Download the Project (Clone the Repository)

In the terminal window, type **exactly**:

```bash
git clone https://github.com/Shnxxx/scraping-trial-test.git
```

Then press **Enter**.

Next, move into the project folder:

```bash
cd scraping-trial-test
```

---

### Step 5 (Optional but Recommended): Create a Virtual Environment

This keeps dependencies isolated.

Type:

```bash
python -m venv .venv
```

Activate it:

- **Windows**:
```bash
.venv\Scripts\activate
```

- **macOS / Linux**:
```bash
source .venv/bin/activate
```

You will see `(.venv)` appear in the terminal.

---

### Step 6: Install Required Libraries

Still in the terminal, type:

```bash
pip install selenium
```

Press Enter and wait until installation finishes.

---

## How to Run the Script

In the same terminal window, inside the project folder, type:

```bash
python scraper.py
```

### What Will Happen

1. Firefox opens automatically
2. A CAPTCHA appears
3. Solve the CAPTCHA **manually**
4. Return to the terminal and press **ENTER**
5. Enter a search term (minimum 3 characters)
   - Press ENTER to use the default `LLC`
6. The script:
   - Navigates all pages
   - Opens each business profile
   - Extracts data
7. Files `output.json` and `output.csv` are created

---

## Search Term Rules

- Minimum of **3 characters**
- Empty searches are not allowed by the site
- Wildcard searches are not supported

Default search term:
```
LLC
```

The user may enter other valid terms such as:
```
Tech
Silver TECH
```

---

## Pagination Handling

- The site displays results across multiple pages (e.g. “Page 1 of 25”)
- The script detects page changes using stable UI text
- All pages are processed automatically

---

## Error Handling & Logging

- Dynamic loading is handled using explicit waits
- Optional fields (agent email) are handled safely
- Errors are logged to:
```
scraper.log
```
- A failed business does **not** stop the script

---

## Performance Notes

- Each business profile opens in a temporary browser tab
- The tab is closed immediately after scraping
- A small delay is added to avoid triggering CAPTCHA again
- Large searches (e.g. 500 records) may take several minutes

This is expected for browser-based scraping.

---

## Limitations

- CAPTCHA must be solved manually
- Resume-after-crash is not implemented
- Browser automation is slower than direct APIs
- Full registry enumeration without search input is impossible

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

Semantic Versioning is used.

- **v1.0.0** – Initial working scraper
- **v1.1.0** – Business profile & agent scraping
- **v1.2.0** – Performance tuning, CSV output, stability improvements

The `main` branch always reflects the latest stable version.

---

## Author’s Notes

### Why Selenium
The site uses dynamic rendering, client-side pagination, and reCAPTCHA.  
A `requests + BeautifulSoup` approach would not reliably capture rendered content.

### CAPTCHA Behavior
After the initial CAPTCHA is solved, the browser session remains valid for a limited time.  
The script relies on this behavior and does **not** attempt to bypass CAPTCHA.

### Pagination Strategy
Waiting directly on table rows caused stale element errors due to React re-renders.  
Stable page indicator text was used instead.

### Resume Capability
Not implemented intentionally.  
CAPTCHA-protected browser sessions make persistent resume logic complex and out of scope.

### Search Scope
The site enforces a minimum search length and disallows wildcard searches.  
The scraper operates strictly within those constraints.

---

## Author

Senjo  
GitHub: https://github.com/Shnxxx
