import pytest
from playwright.sync_api import sync_playwright, Playwright, Page, expect


def test_empty_courses_list(chromium_page_with_state):
    # Используем фикстуру для получения страницы
    page = chromium_page_with_state

    # Переход на страницу курсов
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверка заголовка "Courses"
    courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_have_text("Courses")

    # Проверка видимости иконки
    empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_view_icon).to_be_visible()

    # Проверка текста "There is no results"
    empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_view_title).to_have_text("There is no results")

    # Проверка текста "Results from the load test pipeline will be displayed here"
    empty_view_description = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(empty_view_description).to_have_text("Results from the load test pipeline will be displayed here")