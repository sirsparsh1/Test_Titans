from utils.driver_factory import DriverFactory
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_cart():

    driver = DriverFactory.get_driver("chrome")
    driver.get("https://automationexercise.com")

    product = ProductsPage(driver)
    cart = CartPage(driver)

    product.open_products_page()
    product.add_first_product_to_cart()

    cart.open_cart()

    assert cart.is_product_in_cart()

    driver.quit()