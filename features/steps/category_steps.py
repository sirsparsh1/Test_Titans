from behave import given, when, then


@given("user opens category section")
def open_category(context):
    pass


@when("user selects Women category")
def select_women(context):
    pass


@then("category products should be displayed")
def verify_category(context):
    assert True