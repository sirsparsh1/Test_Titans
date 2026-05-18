from behave import when, then
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@when('user adds product to cart')
def add_product(context):

    ProductsPage(
        context.driver
    ).add_first_product_to_cart()

    CartPage(
        context.driver
    ).open_cart()


@then('product should be visible in cart')
def verify_cart(context):

    assert CartPage(
        context.driver
    ).is_product_in_cart()