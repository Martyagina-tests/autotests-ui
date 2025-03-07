import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement


class Button(BaseElement):
    @property
    def type_of(self) -> str:  # Переопределяем свойство type_of
        return "button"

    def check_enabled(self, nth: int = 0, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" is enabled'):  # Добавили шаг
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_disabled()

    def check_disabled(self, nth: int = 0, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" is disabled'):  # Добавили шаг
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_disabled()