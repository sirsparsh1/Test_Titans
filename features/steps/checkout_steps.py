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

    # Open cart
    page.open_cart()

    # Proceed to checkout
    page.proceed_checkout()

    # Click Register / Login
    page.click_register_login()

    # Login page
    login = LoginPage(
        context.driver
    )

    # Login with valid credentials
    login.login(
    "shaikmusharaf0106@gmail.com",
    "Musharaf@123"
    )

    # Wait after login
    context.driver.implicitly_wait(10)

    # Reopen cart after login
    page.open_cart()

    # Proceed checkout again
    page.proceed_checkout()

    # Wait for checkout page
    page.wait_for_page_load()

    # Add comment
    page.add_comment(
        "Automation Test Order"
    )

    # Place order
    page.place_order()
    page.enter_payment_details()
   

@then("order should place successfully")
def verify_order(context):

    
    context.driver.implicitly_wait(15)

    current_url = context.driver.current_url

    print("CURRENT URL:", current_url)

    assert "payment_done" in current_url