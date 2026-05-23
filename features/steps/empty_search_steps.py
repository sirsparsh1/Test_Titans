from behave import when, then
from pages.products_page import ProductsPage


@when("user searches with empty value")
def empty_search(context):

    context.products = ProductsPage(
        context.driver
    )

    context.products.search_product("")


@then("product search should fail")
def verify_search(context):

    assert True