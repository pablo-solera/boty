from datetime import date
from dotenv import load_dotenv
import os
from playwright.sync_api import sync_playwright

load_dotenv()
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://7imer7ask.audatex.es")

    # Do login
    page.locator("input[type='text']").fill(os.getenv("TIMERTASK_USERNAME"))
    page.locator("input[type='password']").fill(os.getenv("TIMERTASK_PASSWORD"))
    page.locator("button[type='submit']").click()

    page.wait_for_url("https://7imer7ask.audatex.es/audatex/index.php")

    # Go to timesheet tab
    page.locator("a[href='https://7imer7ask.audatex.es/audatex/index.php/imputacion_horas']").click()

    # Fill hours today
    today_day = date.today().day
    page.locator(f"input[data-dia='{today_day}']").fill("8:00")

    # To lose focus and save value
    page.locator("h1").click()
    print("Done!")
    browser.close()