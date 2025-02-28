import pytest
from playwright.sync_api import  Page, Playwright

@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()
        browser.close()

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    """
    Фикстура для регистрации пользователя и сохранения состояния браузера.
    Выполняется один раз за сессию.
    """
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

    # Нажатие на кнопку регистрации
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Сохранение состояния браузера в файл
    context.storage_state(path="browser-state.json")

    # Закрытие контекста и браузера
    context.close()
    browser.close()


@pytest.fixture
def chromium_page_with_state(playwright: Playwright) -> Page:
    """
    Фикстура для создания новой страницы с сохранённым состоянием браузера.
    Выполняется для каждого теста.
    """
    # Создание контекста с сохранённым состоянием
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")  # Использование сохранённого состояния
    page = context.new_page()  # Создание страницы

    yield page  # Возвращаем страницу для использования в тестах

    # Закрытие контекста после завершения теста
    context.close()
    browser.close()