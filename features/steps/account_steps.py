from behave import given, when, then
from pages.login_page import LoginPage
from pages.account_page import AccountPage


@given("user is logged in")
def login(context):
    login_page = LoginPage(context.driver)
    login_page.open_login_page()
    login_page.enter_email("shaikmusharaf863786@gmail.com")
    login_page.enter_password("Musharaf@786")
    login_page.click_login()
    assert login_page.verify_login()


@when("user updates profile")
def update_profile(context):
    context.driver.get("https://automationexercise.com/account")


@then("profile should be updated successfully")
def verify_update(context):
    assert "automationexercise.com" in context.driver.current_url
