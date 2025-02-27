from playwright.sync_api import sync_playwright, expect
from time import sleep
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

    # Регистрация
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Сохранение состояния браузера - в json
    context.storage_state(path="browser-state.json")



with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")


    courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_have_text("Courses")

    # Иконка ( еще можно to_be_attached() , to_be_in_viewport() )
    icon_folder= page.get_by_test_id("courses-list-empty-view-icon")
    expect(icon_folder).to_be_visible()

    # Проверяем текст
    no_results_title = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(no_results_title).to_have_text("There is no results")

    # Проверяем еще текст
    description_text=page.get_by_test_id("courses-list-empty-view-description-text")
    expect(description_text).to_have_text("Results from the load test pipeline will be displayed here")

