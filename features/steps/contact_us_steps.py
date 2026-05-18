from behave import given, when, then
from pages.home_page import HomePage
from pages.contact_us_page import ContactUsPage

@given(u'user opens contact us page')
def step_impl(context):
    HomePage(context.driver).click(HomePage.CONTACT_US_LINK)

@when(u'user submits contact form')
def step_impl(context):
    ContactUsPage(context.driver).submit_form("Test User", "test@example.com", "Test Message")

@then(u'success message should display')
def step_impl(context):
    assert ContactUsPage(context.driver).verify_success()