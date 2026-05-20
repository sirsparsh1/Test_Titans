from behave import *
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage


@given("product already added to cart")
def step_add_product(context):

    context.products = ProductsPage(
        context.driver
    )

    context.products.open_products_page()

    context.products.add_first_product_to_cart()


@when("user proceeds to checkout")
def checkout(context):

    page = CheckoutPage(
        context.driver
    )

    page.open_cart()

    page.proceed_checkout()

    # Popup appears here
    page.click_register_login()

    # Login user
    login = LoginPage(
        context.driver
    )

    login.login(
        "testuser@gmail.com",
        "test@123"
    )

    # Return to cart
    page.open_cart()

    page.proceed_checkout()

    # Add comment
    page.add_comment()

    # Place order
    page.place_order()


@then("order should place successfully")
def verify_order(context):

    page = CheckoutPage(
        context.driver
    )

    assert page.is_order_successful()