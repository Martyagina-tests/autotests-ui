from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.input import Input

class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Input(page,'create-course-form-title-input', "Create course")
        self.estimated_time = Input(page,'create-course-form-estimated-time-input', "Estimated time")
        self.description_textarea = Input(page, 'create-course-form-description-input', 'Description')
        self.max_score_input = Input(page,'create-course-form-max-score-input', "Max Score")
        self.min_score_input = Input(page,'create-course-form-min-score-input', "Min Score")

    def fill(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title.fill(title)
        self.estimated_time.fill(estimated_time)
        self.description_textarea.fill(description)
        self.max_score_input.fill(max_score)
        self.min_score_input.fill(min_score)

    def check_visible(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title.check_visible()
        self.title.check_have_value(title)
        self.estimated_time.check_visible()
        self.estimated_time.check_have_text(estimated_time)
        self.description_textarea.check_visible()
        self.description_textarea.check_have_text(description)
        self.min_score_input.check_visible()
        self.min_score_input.check_have_text(min_score)
        self.max_score_input.check_visible()
        self.max_score_input.check_have_text(max_score)





