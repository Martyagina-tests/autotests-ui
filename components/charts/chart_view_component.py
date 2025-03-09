from playwright.sync_api import Page, expect
import allure

class ChartViewComponent:
    def __init__(self, page: Page, identifier: str, chart_type: str):
        self.identifier = identifier
        self.chart_type = chart_type

        # Динамические локаторы
        self.title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')


    @allure.step('Check visible chart "{expected_title}"')
    def check_visible(self, expected_title: str):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(expected_title)
        expect(self.chart).to_be_visible()