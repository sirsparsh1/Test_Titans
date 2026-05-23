from behave import given
from pages.products_page import ProductsPage


@given('the browser is open')
def open_browser(context):
    pass


@given('user navigates to AutomationExercise website')
def open_site(context):

    context.driver.get(
        "https://automationexercise.com"
    )


@given('user opens products page')
def open_products(context):

    context.driver.get(
        "https://automationexercise.com/products"
    )

    context.products_page = ProductsPage(
        context.driver
    )