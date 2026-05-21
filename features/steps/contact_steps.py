from behave import given, when, then

@given('user opens contact us page')
def step_impl(context):
    print("Opening contact us page")

@when('user submits contact form')
def step_impl(context):
    print("Submitting contact form")

@then('success message should display')
def step_impl(context):
    print("Validating success message")