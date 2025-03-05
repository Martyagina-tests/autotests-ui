
import pytest
from playwright.sync_api import Page
from pages.dashboard_page import DashboardPage

@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_displaying(page: Page):
    # Параметры для графика
    identifier = "students"
    chart_type = "bar"
    expected_title = "Students"

    # Инициализация DashboardPage
    dashboard_page = DashboardPage(page, identifier=identifier, chart_type=chart_type)

    # Переход на страницу dashboard
    dashboard_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    # Проверка видимости sidebar
    dashboard_page.sidebar.check_visible()

    # Проверка видимости графика и заголовка
    dashboard_page.chart_view.check_visible(expected_title)