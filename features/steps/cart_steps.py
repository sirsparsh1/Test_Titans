from behave import when, then
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@when('user adds product to cart')
def add_cart(context):

    product = ProductsPage(
        context.driver
    )

    product.add_first_product_to_cart()


@then('product should be visible in cart')
def verify_cart(context):

    cart = CartPage(context.driver)

    cart.open_cart()

    assert cart.is_product_in_cart()