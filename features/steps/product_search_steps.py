from behave import given, when, then
from pages.products_page import ProductsPage


@given('user opens products page')
def open_products(context):
    ProductsPage(context.driver).open_products_page()


@when('user searches product "{product}"')
def search_product(context, product):
    ProductsPage(context.driver).search_product(product)


@then('searched product should display')
def verify_product(context):
    assert ProductsPage(context.driver).is_product_visible()