import allure
import pytest

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory # Импортируем enum AllureStory
from tools.allure.tags import AllureTag
from allure_commons.types import Severity

@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.suite(AllureFeature.AUTHENTICATION)# Добавили feature
@allure.story(AllureStory.AUTHORIZATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)# Добавили story
class TestAuthorization:
    @allure.title("User login with correct email and password")
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(
            self,
            login_page: LoginPage,
            dashboard_page: DashboardPage,
            registration_page: RegistrationPage):

        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(email="user.name@gmail.com", username="username", password="password")
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email="user.name@gmail.com", password="password")
        login_page.click_login_button()

        # Проверка элементов Dashboard после входа
        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()


    @pytest.mark.parametrize(
        "email, password",
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail.com", "  "),
            ("  ", "password")
        ]
    )
    @allure.tag("USER_LOGIN")
    @allure.title("Wrong_email_or_password")
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.login_form.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    @pytest.mark.regression
    @pytest.mark.authorization
    @allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
    @allure.epic(AllureEpic.LMS)
    @allure.feature(AllureFeature.AUTHENTICATION)
    @allure.story(AllureStory.AUTHORIZATION)
    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_registration_link()
        registration_page.registration_form.check_visible(email="", username="", password="")

