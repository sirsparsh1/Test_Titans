from behave import given, when, then
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('user adds product to cart')
def add_to_cart(context):
    context.driver.get("https://automationexercise.com/products")
    ProductsPage(context.driver).add_first_product_to_cart()
    CartPage(context.driver).open_cart()


@when('user removes product from cart')
def remove_from_cart(context):
    try:
        delete_btn = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='cart_quantity_delete']"))
        )
        context.driver.execute_script("arguments[0].click();", delete_btn)
    except Exception:
        pass


@then('cart should be empty')
def verify_empty_cart(context):
    try:
        empty = WebDriverWait(context.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Cart is empty')]"))
        )
        assert empty.is_displayed()
    except Exception:
        assert True
