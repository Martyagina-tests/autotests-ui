from typing import Pattern
from playwright.sync_api import Page
from components.base_component import BaseComponent
from  elements.icon import Icon
from elements.text import Text
from elements.button import Button
import allure

class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):  # Принимаем identifier при создании
        super().__init__(page)
        self.identifier = identifier  # Сохраняем identifier

        self.icon = Icon(page, f'{self.identifier}-drawer-list-item-icon', "Item icon")
        self.title = Text(page, f'{self.identifier}-drawer-list-item-title-text', "Item title")
        self.button = Button(page, f'{self.identifier}-drawer-list-item-button', "Item Button")

    @allure.step('Check visible "title" sidebar list item')
    def check_visible(self, title: str):
        self.icon.check_visible()
        self.title.check_visible()
        self.title.check_have_text(title)
        self.button.check_visible()


    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)