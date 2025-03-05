from playwright.sync_api import Page, expect

from components.base_component import BaseComponent

class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.estimated_time_input = (
            page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        )
        self.description_textarea = (
            page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        )
        self.max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')

    def fill(self, title_input: str, estimated_time_input: str, description_textarea: str, max_score_input: str, min_score_input: str):
        self.title_input.fill(title_input)
        self.estimated_time_input.fill(estimated_time_input)
        self.description_textarea.fill(description_textarea)
        self.max_score_input.fill(max_score_input)
        self.min_score_input.fill(min_score_input)

    def check_visible(self, title_input: str, estimated_time_input: str, description_textarea: str, max_score_input: str, min_score_input: str):
        expect.title_input(self.title_input).to_be_visiable()
        expect.estimated_time_input(self.estimated_time_input).to_be_visiable()
        expect.description_textarea(self.description_textarea).to_be_visiable()
        expect.max_score_input(self.max_score_input).to_be_visiable()
        expect.min_score_input(self.min_score_input).to_be_visiable()




