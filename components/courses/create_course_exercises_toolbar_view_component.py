import allure
from playwright.sync_api import Page
from elements.text import Text
from elements.button import Button

class CreateExerciseToolbarViewComponent:
    def __init__(self, page: Page):
        self.title = Text(page,'create-course-exercises-box-toolbar-title-text', "Exercises")
        self.button = Button(page,'create-course-exercises-box-toolbar-create-exercise-button', "Create exercise button")

    @allure.step('Check visible empty create exercise form')
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Exercises')
        self.button.check_visible()


    def click_create_course_button(self):
        self.button.click()
