import pytest
from playwright.sync_api import sync_playwright, Page, Playwright

def test_wrong_email_or_password_authorization(chromium_page: Page):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill('user.name.gmail.com')

    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill('password')

    login_button = chromium_page.get_by_test_id('login-page-login-button')
    login_button.click()
