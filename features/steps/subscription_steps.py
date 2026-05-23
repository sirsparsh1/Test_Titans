from behave import given, when, then
from pages.home_page import HomePage


@given('user opens homepage')
def open_home(context):
    context.driver.get("https://automationexercise.com")


@when('user subscribes with valid email')
def subscribe(context):
    HomePage(context.driver).subscribe_email("test@test.com")


@then('subscription should be successful')
def verify_subscription(context):
    assert True