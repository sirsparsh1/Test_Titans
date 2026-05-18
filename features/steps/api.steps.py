from behave import given, when, then
import requests

@given('products API endpoint')
def products_api(context):

    context.url = (
        "https://automationexercise.com/api/productsList"
    )


@when('user sends GET request')
def send_request(context):

    context.response = requests.get(context.url)


@then('API response status should be 200')
def verify_status(context):

    assert context.response.status_code == 200