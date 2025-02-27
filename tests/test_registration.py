from playwright.sync_api import sync_playwright, expect

def test_successful_registration():
    with sync_playwright() as playwright:
        # Запуск браузера и создание контекста
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()  # Создание контекста
        page = context.new_page()  # Создание страницы

        # Открытие страницы регистрации
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Заполнение полей регистрации
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        # Регистрация -
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Сохранение состояния браузера - в json
        context.storage_state(path="browser-state.json")