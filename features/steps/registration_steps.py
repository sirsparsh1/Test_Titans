from behave import when, then
from pages.register_page import RegisterPage
import random
import time

@when('user enters valid registration details')
def enter_registration(context):

    context.register_page = RegisterPage(context.driver)
    email = f"test_{int(time.time())}@mail.com"

    

    context.register_page.register_user(
        "Shaik Musharaf",
        email,
        "Musharaf@123"
    )


@then('account should be created successfully')
def verify_registration(context):

    assert context.register_page.verify_account_created() is True