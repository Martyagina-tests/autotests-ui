import allure

from playwright.sync_api import expect
from elements.base_element import BaseElement
from tools.logger import get_logger
from ui_coverage_tool import ActionType

logger = get_logger("BUTTON")

class Button(BaseElement):
    @property
    def type_of(self) -> str:  # Переопределяем свойство type_of
        return "button"

    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        # Переопределяем метод формирования XPath-селектора:
        #  - сначала получаем общий селектор блока
        #  - затем уточняем путь до самого <input>, добавляя '//input'
        # Это нужно, чтобы трекер точно знал, с каким элементом шло взаимодействие.
        return f'{super().get_raw_locator(**kwargs)}//button'

    def check_enabled(self, nth: int = 0, **kwargs):

        step = f'Checking that {self.type_of} "{self.name}" is enabled'
        with allure.step(step):  # Добавили шаг
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)  # Добавили логирование
            expect(locator).to_be_disabled()

        self.track_coverage(ActionType.ENABLED, nth, **kwargs)

    def check_disabled(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is disabled'
        with allure.step(step):  # Добавили шаг
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_disabled()

        self.track_coverage(ActionType.DISABLED, nth, **kwargs)