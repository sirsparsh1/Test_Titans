from behave import when, then
from pages.products_page import ProductsPage


@when('user searches product "{product}"')
def search_product(context, product):

    context.products_page = ProductsPage(
        context.driver
    )

    context.products_page.search_product(
        product
    )


@then('searched product should display')
def verify_product(context):

    assert context.products_page.is_product_visible()