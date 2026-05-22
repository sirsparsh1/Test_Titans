from behave import given, then


@given('user opens test cases page')
def open_testcases(context):

    context.driver.get(
        "https://automationexercise.com/test_cases"
    )


@then('page title should be visible')
def verify_page(context):

    assert "Test Cases" in context.driver.page_source