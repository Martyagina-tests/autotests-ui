import pytest

@pytest.mark.parametrize(
    "email, password",
    [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password"),
    ],
    ids=[
        "Невалидные email и password",
        "Невалидный email и пустой password",
        "Пустой email и невалидный password",
    ]
)
def test_wrong_email_or_password_authorization_1(email: str, password: str):
    pass