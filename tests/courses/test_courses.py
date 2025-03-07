import pytest

from pages.courses.courses_list_page  import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
class TestAuthorization:
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.fill_create_course_form(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )

        # Шаг 3: Нажать кнопку создания курса
        create_course_page.click_create_course_button()

        # Шаг 4: Проверить, что карточка курса отображается с правильными данными
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )

        # Шаг 5: Открыть меню карточки курса и нажать "Edit"
        courses_list_page.course_view_menu.click_edit(index=0)

        # Шаг 6: Заполнить форму редактирования курса новыми данными
        create_course_page.fill_create_course_form(
            title="Playwright1",
            estimated_time="3 weeks",
            description="Playwright_",
            max_score="1000",
            min_score="100"
        )

        # Шаг 7: Нажать кнопку сохранения изменений
        create_course_page.click_create_course_button()

        # Шаг 8: Проверить, что карточка курса обновлена с новыми данными
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright1",
            max_score="1000",
            min_score="100",
            estimated_time="3 weeks"
        )


    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        # Шаг 1: Открыть страницу создания курса
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=True)

        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)

        # Шаг 4: Проверить, что форма создания курса отображается с пустыми значениями
        create_course_page.check_visible_create_course_form(
            title="", max_score="0", min_score="0", description="", estimated_time=""
        )

        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')

        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        # Шаг 7: Заполнить форму создания курса
        create_course_page.fill_create_course_form(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )

        # Шаг 8: Нажать кнопку создания курса
        create_course_page.click_create_course_button()

        # Шаг 9: Проверить, что курс создан
        courses_list_page.course_view.check_visible(
            index=0,  # Указываем индекс курса (например, 0 для первого курса)
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )

    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_page.sidebar.check_visible()
        courses_list_page.navbar.check_visible("username")
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

