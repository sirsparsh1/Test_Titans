from behave import given, when, then
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage


@given('product already added to cart')
def cart_ready(context):

    product = ProductsPage(context.driver)

    product.open_products_page()
    product.add_first_product_to_cart()


@when('user proceeds to checkout')
def checkout(context):

    page = CheckoutPage(context.driver)

    page.place_order()
    page.fill_payment_details()


@then('order should place successfully')
def verify_order(context):

    page = CheckoutPage(context.driver)

    assert page.is_order_successful()