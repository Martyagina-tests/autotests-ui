from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button

class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_button = Button(page,'create-course-toolbar-create-course-button', "Create course button")

    def check_visible(self, is_create_course_disabled: bool = True):
        self.create_course_button.check_visible()

        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        else:
            self.create_course_button.check_enabled()

    def click_create_course_button(self):
        self.create_course_button.click()

