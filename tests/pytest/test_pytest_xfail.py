import pytest


@pytest.mark.xfail(reason='Найден баг в приложении, из-за которого тест падает с ошибкой')
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason='Баг уже исправлен, но на тест все еще висит маркировка xfail') # Если будет XPASS , то можно заменить маркировку
def test_without_bug():
    pass