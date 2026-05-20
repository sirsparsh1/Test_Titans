from utils.driver_factory import DriverFactory
from pages.products_page import ProductsPage


def test_product_search():

    driver = DriverFactory.get_driver("chrome")
    driver.get("https://automationexercise.com")

    product = ProductsPage(driver)

    product.open_products_page()
    product.search_product("Blue Top")

    assert product.is_product_visible()

    driver.quit()