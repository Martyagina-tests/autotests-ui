import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.input import Input
from elements.button import Button

class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page,'registration-form-email-input', "email")
        self.username_input = Input(page,'registration-form-username-input',"username")
        self.password_input = Input(page,'registration-form-password-input', "password")
        self.registration_button = Button(page,'registration-page-registration-button',"Registration")

    @allure.step("Fill registration form")
    def fill(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)

    @allure.step("Check visible registration form")
    def check_visible(self, email: str, username: str, password: str):
        self.email_input.check_visible()
        self.email_input.check_have_value(email)
        self.username_input.check_visible()
        self.username_input.check_have_value(username)
        self.password_input.check_visible()
        self.password_input.check_have_value(password)
