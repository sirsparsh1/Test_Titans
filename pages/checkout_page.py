from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    CART_LINK = (
        By.XPATH,
        "//a[@href='/view_cart']"
    )

    CHECKOUT = (
        By.XPATH,
        "//a[contains(text(),'Proceed To Checkout')]"
    )

    PLACE_ORDER = (
        By.XPATH,
        "//a[contains(text(),'Place Order')]"
    )

    def open_cart(self):

        self.click(self.CART_LINK)

    def place_order(self):

        self.open_cart()

        self.click(self.CHECKOUT)

        self.click(self.PLACE_ORDER)