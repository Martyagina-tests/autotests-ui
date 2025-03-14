import pytest

@pytest.mark.smoke
def test_smoke_case():
    ...

#@pytest.mark.regression
def test_regression_case():
    ...

@pytest.mark.fast
def test_fast():
    pass

@pytest.mark.slow
def test_slow():
    pass

@pytest.mark.smoke # Для класса
class TestSuite:
    def test_case1(self):
        ...

    def test_case2(self):
        ...


import pytest


# @pytest.mark.regression # Для класса и внутри класса у каждой функции своя
class TestUserAuthentication:

    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):
        pass

    def test_logout(self):
        pass

    @pytest.mark.smoke   # У одной функции несколько маркировок
    #@pytest.mark.regression
    @pytest.mark.critical
    def test_critical_login(self):
        pass

@pytest.mark.ui   # У одной функции несколько маркировок + маркировка для класса
class TestUserInterface:

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_button(self):
        pass

    # @pytest.mark.regression
    def test_forgot_password_link(self):
        pass

