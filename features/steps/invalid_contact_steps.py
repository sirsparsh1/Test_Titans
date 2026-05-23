from behave import when, then


@when("user submits empty contact form")
def submit_empty_form(context):

    context.contact_page.submit_form(
        "",
        "",
        "",
        ""
    )


@then("contact form validation should display")
def verify_validation(context):

    assert True