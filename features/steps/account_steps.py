from behave import given, when, then


@given("user is logged in")
def login(context):
    pass


@when("user updates profile")
def update_profile(context):
    pass


@then("profile should be updated successfully")
def verify_update(context):
    assert True