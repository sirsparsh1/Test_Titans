from behave import given, when, then
from pages.contact_us_page import ContactUsPage


@given('user opens contact us page')
def open_contact(context):
    context.driver.get(
        "https://automationexercise.com/contact_us"
    )


@when('user submits contact form')
def submit_contact(context):

    context.contact_page = ContactUsPage(context.driver)

    context.contact_page.submit_form(
        "Shaik",
        "shaik@gmail.com",
        "Automation Testing"
    )


@then('success message should display')
def verify_success(context):

    assert context.contact_page.verify_success()