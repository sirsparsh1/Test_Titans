from behave import given

@given('the browser is open')
def open_browser(context):
    pass  # driver already started in environment.py


@given('user navigates to AutomationExercise website')
def open_site(context):
    context.driver.get("https://automationexercise.com")