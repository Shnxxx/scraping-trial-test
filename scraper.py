from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import logging


DEFAULT_SEARCH_TERM = "LLC"


# -----------------------------
# 1. LOGGING SETUP (REQUIRED)
# -----------------------------
logging.basicConfig(
    filename="scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------
# 2. BROWSER SETUP
# -----------------------------
service = Service()
driver = webdriver.Firefox(service=service)
driver.maximize_window()

try:
    # -----------------------------
    # 3. OPEN SITE + CAPTCHA
    # -----------------------------
    driver.get("https://scraping-trial-test.vercel.app/search")
    input("Solve the CAPTCHA manually, then press ENTER here...")

    # -----------------------------
    # 4. PERFORM SEARCH
    # -----------------------------
    search_input = driver.find_element(By.TAG_NAME, "input")
    while True:
        search_term = input(
            f"Enter search term (min 3 chars) [default: {DEFAULT_SEARCH_TERM}]: "
        ).strip()

        if not search_term:
            # User pressed ENTER → use default
            search_term = DEFAULT_SEARCH_TERM
            break

        if len(search_term) < 3:
            print("Search term must be at least 3 characters. Please try again.")
            continue

        # Valid custom search term
        break

    search_input.send_keys(search_term)

    search_button = driver.find_element(By.TAG_NAME, "button")
    search_button.click()

    # INITIAL LOAD WAIT (use EC, no lambda)
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table"))
    )

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr"))
    )

    # -----------------------------
    # 5. SCRAPE ALL PAGES
    # -----------------------------
    all_records = []

    while True:
        # -----------------------------
        # SCRAPE CURRENT PAGE
        # -----------------------------
        rows = driver.find_elements(By.CSS_SELECTOR, "tbody tr")

        if not rows:
            break

        # -----------------------------
        # EXTRACT ALL ROWS ON PAGE
        # -----------------------------
        for row in rows:
            try:
                cells = row.find_elements(By.TAG_NAME, "td")

                record = {
                    "business_name": cells[0].text,
                    "registration_id": cells[1].text,
                    "status": cells[2].text,
                    "filing_date": cells[3].text
                }

                all_records.append(record)

            except Exception as e:
                logging.error(f"Failed to parse row: {e}")

        # -----------------------------
        # PAGINATION (UI TEXT BASED, FINAL)
        # -----------------------------
        current_page_text = driver.find_element(
            By.CSS_SELECTOR,
            ".table-meta .small.muted:last-child"
        ).text  # e.g. "Page 25 of 25"

        next_button = driver.find_element(By.XPATH, "//button[text()='Next']")
        next_button.click()

        try:
            WebDriverWait(driver, 15).until(
                lambda d: d.find_element(
                    By.CSS_SELECTOR,
                    ".table-meta .small.muted:last-child"
                ).text != current_page_text
            )
        except TimeoutException:
            # We are on the last page; stop pagination
            break

    # -----------------------------
    # 7. SAVE OUTPUT
    # -----------------------------
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(all_records, f, indent=2)

    logging.info(f"Scraping completed. Total records: {len(all_records)}")
    print(f"Done. Scraped {len(all_records)} records.")

finally:
    # -----------------------------
    # 8. CLEANUP
    # -----------------------------
    driver.quit()

