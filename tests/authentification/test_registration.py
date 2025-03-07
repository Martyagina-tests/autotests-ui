import allure
import pytest

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory # Импортируем enum AllureStory
from tools.allure.tags import AllureTag
from allure_commons.types import Severity


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.dashboard
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.parent_suite(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION) # Добавили feature
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION) # Добавили story
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @allure.tag(AllureTag.REGISTRATION, AllureTag.REGRESSION)
    @allure.title("Registration with correct email, username and password")
    @allure.severity(Severity.CRITICAL)    # Добавили заголовок
    def test_successful_registration(self, dashboard_page: DashboardPage, registration_page: RegistrationPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(
            email="user.name@gmail.com",
            username="username",
            password="password"
        )
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view.check_visible()

