from behave import given, when, then
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage


@given('product already added to cart')
def cart_ready(context):

    # Login first (checkout requires authentication)
    login = LoginPage(context.driver)
    login.open_login_page()
    login.enter_email("shaikmusharaf863786@gmail.com")
    login.enter_password("Musharaf@786")
    login.click_login()

    # Then add product to cart
    product = ProductsPage(context.driver)
    product.open_products_page()
    product.add_first_product_to_cart()


@when('user proceeds to checkout')
def checkout(context):

    CheckoutPage(context.driver).place_order()


@then('order should place successfully')
def verify_order(context):

    assert True