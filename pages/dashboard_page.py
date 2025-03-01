from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def check_dashboard_title_is_visible(self):
        dashboard_title = self.page.get_by_test_id("dashboard-toolbar-title-text")
        expect(dashboard_title).to_be_visible()