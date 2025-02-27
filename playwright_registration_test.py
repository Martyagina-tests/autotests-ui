from playwright.sync_api import sync_playwright, expect
from time import sleep

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()