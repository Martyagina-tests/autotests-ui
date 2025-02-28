import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list():
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

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
        expect(courses_title).to_have_text("Courses")

        # Иконка ( еще можно to_be_attached() , to_be_in_viewport() )
        empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_view_icon).to_be_visible()

        # Проверяем текст
        empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(empty_view_title).to_have_text("There is no results")

        # Проверяем еще текст
        empty_view_description = page.get_by_test_id("courses-list-empty-view-description-text")
        expect(empty_view_description).to_have_text("Results from the load test pipeline will be displayed here")