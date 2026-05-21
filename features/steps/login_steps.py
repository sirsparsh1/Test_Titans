from behave import given, when, then
from pages.login_page import LoginPage


@given('user opens signup login page')
def open_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open_login_page()


@when('user enters email "{email}"')
def enter_email(context, email):
    context.login_page.enter_email(email)


@when('user enters password "{password}"')
def enter_password(context, password):
    context.login_page.enter_password(password)


@when('user clicks login button')
def click_login(context):
    context.login_page.click_login()


@then('user should login successfully')
def verify_login(context):
    assert context.login_page.verify_login() is True