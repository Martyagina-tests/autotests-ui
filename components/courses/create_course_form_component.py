from playwright.sync_api import Page, expect

from components.base_component import BaseComponent

class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.estimated_time = (
            page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        )
        self.description_textarea = (
            page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        )
        self.max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')

    def fill(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title.fill(title)
        self.estimated_time.fill(estimated_time)
        self.description_textarea.fill(description)
        self.max_score_input.fill(max_score)
        self.min_score_input.fill(min_score)

    def check_visible(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)
        expect(self.estimated_time).to_be_visible()
        expect(self.description_textarea).to_be_visible()
        expect(self.max_score_input).to_be_visible()
        expect(self.min_score_input).to_be_visible()




