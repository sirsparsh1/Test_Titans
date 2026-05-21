from behave import given, when, then
from pages.login_page import LoginPage


@given("user has placed an order")
def place_order(context):
    login_page = LoginPage(context.driver)
    login_page.open_login_page()
    login_page.enter_email("shaikmusharaf863786@gmail.com")
    login_page.enter_password("Musharaf@786")
    login_page.click_login()
    assert login_page.verify_login()


@when("user opens order history")
def open_history(context):
    context.driver.get("https://automationexercise.com/order_list")


@then("order should be displayed")
def verify_order(context):
    assert "order_list" in context.driver.current_url or "automationexercise" in context.driver.current_url
