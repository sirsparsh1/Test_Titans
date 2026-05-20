from utils.driver_factory import DriverFactory
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_checkout():

    driver = DriverFactory.get_driver("chrome")
    driver.get("https://automationexercise.com")

    product = ProductsPage(driver)
    cart = CartPage(driver)

    product.open_products_page()
    product.add_first_product_to_cart()

    cart.open_cart()
    cart.proceed_to_checkout()

    assert "checkout" in driver.current_url.lower()

    driver.quit()