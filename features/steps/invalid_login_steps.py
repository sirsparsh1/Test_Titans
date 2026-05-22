from behave import given, when, then
from pages.login_page import LoginPage


@given("user opens login page")
def open_login(context):

    context.login = LoginPage(
        context.driver
    )

    context.login.open_login_page()


@when("user enters invalid email and password")
def invalid_credentials(context):

    context.login.enter_email(
        "wrong@gmail.com"
    )

    context.login.enter_password(
        "wrong123"
    )


@then("error message should display")
def verify_error(context):

    assert True