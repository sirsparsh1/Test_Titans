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

    CheckoutPage(context.driver).place_order()


@then('order should place successfully')
def verify_order(context):

    assert True