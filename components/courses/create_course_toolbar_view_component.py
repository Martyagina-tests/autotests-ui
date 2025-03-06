from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

    def check_visible(self, is_create_course_disabled: bool = True):
        expect(self.create_course_button).to_be_visible()
        if is_create_course_disabled:
            expect(self.create_course_button).to_be_disabled()
        else:
            expect(self.create_course_button).to_be_enabled()

    def click_create_course_button(self):
        self.create_course_button.click()

