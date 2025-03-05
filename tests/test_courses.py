import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    # Шаг 1: Открыть страницу создания курса
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

    # Шаг 2: Проверить, что кнопка создания курса недоступна
    create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=True)

    # Шаг 3: Заполнить форму создания курса
    create_course_page.create_course_form.fill(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )

    # Шаг 4: Проверить, что кнопка создания курса доступна
    create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=False)

    create_course_page.image_upload_widget.upload_preview_image()

    # Шаг 5: Нажать кнопку создания курса
    create_course_page.create_course_toolbar_view.click_create_course_button()

    # Шаг 6: Проверить, что курс создан
    courses_list_page.course_view.check_visible(
        index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
    )

def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    courses_list_page.sidebar.check_visible()
    courses_list_page.navbar.check_visible("username")
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.check_visible_empty_view()