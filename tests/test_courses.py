import pytest
from pages.courses_list_page import CoursesListPage, Page, expect
from pages.create_course_page import CreateCoursePage

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    # Шаг 1: Открыть страницу создания курса
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

    # Шаг 2: Проверить заголовок "Create Course"
    create_course_page.check_visible_create_course_title()

    # Шаг 3: Проверить, что кнопка создания курса недоступна
    create_course_page.check_disabled_create_course_button()

    # Шаг 4: Проверить пустой блок предпросмотра изображения
    create_course_page.check_visible_image_preview_empty_view()

    # Шаг 5: Проверить блок загрузки изображения
    create_course_page.check_visible_image_upload_view()

    # Шаг 6: Проверить форму создания курса
    create_course_page.check_visible_create_course_form()

    # Шаг 7: Проверить заголовок "Exercises"
    create_course_page.check_visible_exercises_title()

    # Шаг 8: Проверить кнопку создания задания
    create_course_page.check_visible_create_exercise_button()

    # Шаг 9: Проверить блок с пустыми заданиями
    create_course_page.check_visible_exercises_empty_view()

    # Шаг 10: Загрузить изображение
    create_course_page.upload_preview_image("./testdata/files/image.png")

    # Шаг 11: Проверить состояние загрузки изображения
    create_course_page.check_visible_image_upload_view()

    # Шаг 12: Заполнить форму создания курса
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )

    # Шаг 13: Нажать кнопку создания курса
    create_course_page.click_create_course_button()

    # Шаг 14: Проверить заголовок "Courses" на странице списка курсов
    courses_list_page.check_visible_courses_title()

    # Шаг 15: Проверить кнопку создания курса
    courses_list_page.check_visible_create_course_button()

    # Шаг 16: Проверить карточку курса
    courses_list_page.check_visible_course_card(
        index=0,
        title="Playwright",
        estimated_time="2 weeks",
        max_score="100",
        min_score="10"
    )

def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    courses_list_page.sidebar.check_visible()
    courses_list_page.navbar.check_visible("username")
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_empty_view()
