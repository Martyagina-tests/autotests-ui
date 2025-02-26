from playwright.sync_api import sync_playwright, expect
from time import sleep

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Открыть страницу
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    #Заполнит поле "Email" значением "user.name@gmail.com"
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill("user.name@gmail.com")

    #Заполнит поле "Username" значением "username"
    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill("username")

    # Заполнит поле "Password" значением "password"
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill("password")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()


    #Редирект
    expect(page).to_have_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    #Дашборд
    dashboard_check =page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_check).to_have_text("Dashboard")
    sleep(5)
