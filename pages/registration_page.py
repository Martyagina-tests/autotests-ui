from playwright.sync_api import Page
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button

class RegistrationPage(BasePage): # Регистрация
    def __init__(self, page: Page):
        super().__init__(page)
        self.registration_form = RegistrationFormComponent(page)
        self.registration_button = Button(page, 'registration-page-registration-button', "Registration")


    # Метод для нажатия на кнопку "Registration"

    def click_registration_button(self):
        self.registration_button.click()