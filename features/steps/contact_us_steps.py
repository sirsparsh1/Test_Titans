from behave import *
from pages.contact_us_page import ContactUsPage


@given("user opens contact us page")
def open_contact(context):

    context.contact_page = ContactUsPage(
        context.driver
    )

    context.contact_page.open_contact_page()


@when("user submits contact form")
def submit_contact(context):

    context.contact_page.submit_form(
        "Shaik",
        "shaik@gmail.com",
        "Automation Testing",
        "This is automation testing message"
    )


@then("success message should display")
def verify_success(context):

    assert context.contact_page.is_success()