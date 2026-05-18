from behave import given, when, then
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@given('user opens products page')
def open_products(context):

    ProductsPage(context.driver).open_products_page()


@when('user adds product to cart')
def add_cart(context):

    ProductsPage(
        context.driver
    ).add_first_product_to_cart()


@then('product should be visible in cart')
def verify_cart(context):

    cart = CartPage(context.driver)

    cart.open_cart()

    assert cart.is_product_in_cart()