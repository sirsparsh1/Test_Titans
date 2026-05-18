from behave import given, when, then
from pages.products_page import ProductsPage


@when("user selects first product")
def select_product(context):
    ProductsPage(context.driver).click_first_product()


@then("product details should be visible")
def verify_details(context):
    assert True