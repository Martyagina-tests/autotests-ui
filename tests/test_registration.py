import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize(
    "email, username, password",
    [
        ("user.name@gmail.com", "успех", "password"),
        ("user123.name@gmail.com", "успех", "password123")
    ],
    ids=[
        "Успешная регистрация первого пользователя",
        "Успешная регистрация второго пользователя"
    ]
)
def test_successful_registration(registration_page: RegistrationPage, email: str, username: str, password: str,
                                 dashboard_page: DashboardPage):
    # Переход на страницу регистрации
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполнение формы регистрации
    registration_page.fill_registration_form(email=email, username=username, password=password)

    # Нажатие на кнопку регистрации
    registration_page.click_registration_button()

    dashboard_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    dashboard_page.check_dashboard_title_is_visible()


