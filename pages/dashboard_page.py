from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.navigation.sidebar_component import SidebarComponent
from components.charts.chart_view_component import ChartViewComponent


class DashboardPage(BasePage):
    def __init__(self, page: Page, identifier: str, chart_type: str ):
        super().__init__(page)
        self.sidebar = SidebarComponent(page)  # Initialize SidebarComponent
        self.chart_view = ChartViewComponent(page, identifier=identifier, chart_type=chart_type)  # Initialize ChartViewComponent with dynamic values