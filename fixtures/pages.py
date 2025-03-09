import pytest
from playwright.sync_api import Page
from pages.courses.courses_list_page import CoursesListPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.courses.create_course_page import CreateCoursePage

@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)

@pytest.fixture
def registration_page(page: Page) -> RegistrationPage:
    return RegistrationPage(page=page)

@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page=page)


@pytest.fixture
def dashboard_page_with_state(page_with_state: Page) -> DashboardPage:
    return DashboardPage(page=page_with_state)

@pytest.fixture
def courses_list_page(page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(page=page_with_state)

# Добавили эту фикстуру в данном шаге
@pytest.fixture
def create_course_page(page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(page=page_with_state)




