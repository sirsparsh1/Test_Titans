from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    CART_LINK = (
        By.XPATH,
        "//a[@href='/view_cart']"
    )

    CART_ITEMS = (
        By.XPATH,
        "//tr[@id='product-1']"
    )

    CHECKOUT_BTN = (
        By.XPATH,
        "//a[contains(text(),'Proceed To Checkout')]"
    )

    def open_cart(self):

        self.click(self.CART_LINK)

    def is_product_in_cart(self):

        return self.driver.find_element(
            *self.CART_ITEMS
        ).is_displayed()

    def proceed_to_checkout(self):

        self.click(self.CHECKOUT_BTN)