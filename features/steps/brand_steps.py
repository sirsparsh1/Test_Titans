from behave import when, then
from pages.products_page import ProductsPage


@when('user selects brand "{brand}"')
def select_brand(context, brand):

    ProductsPage(context.driver).select_brand(brand)


@then("brand products should be displayed")
def verify_brand(context):

    assert ProductsPage(
        context.driver
    ).is_brand_page_displayed()