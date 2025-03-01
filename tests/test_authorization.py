import pytest
from pages.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
    "email, password",
    [
        ("user.name@gmail.com", "password"),  # Невалидные email и password
        ("user.name@gmail.com", "  "),       # Невалидный email и пустой password
        ("  ", "password"),                  # Пустой email и невалидный password
    ],
    ids=[
        "Невалидные email и password",
        "Невалидный email и пустой password",
        "Пустой email и невалидный password",
    ]
)
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    # Переход на страницу авторизации
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Заполнение формы авторизации
    login_page.fill_login_form(email=email, password=password)

    # Нажатие на кнопку входа
    login_page.click_login_button()

    # Проверка сообщения об ошибке
    login_page.check_visible_wrong_email_or_password_alert()