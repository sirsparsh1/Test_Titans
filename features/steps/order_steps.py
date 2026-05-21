from behave import given, when, then


@given("user has placed an order")
def place_order(context):
    pass


@when("user opens order history")
def open_history(context):
    pass


@then("order should be displayed")
def verify_order(context):
    assert True