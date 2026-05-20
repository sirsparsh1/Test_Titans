from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    CART_BUTTON = (
        By.XPATH,
        "//a[@href='/view_cart']"
    )

    PROCEED_TO_CHECKOUT = (
        By.XPATH,
        "//a[contains(text(),'Proceed To Checkout')]"
    )

    REGISTER_LOGIN = (
        By.XPATH,
        "//u[contains(text(),'Register / Login')]"
    )

    COMMENT_BOX = (
        By.NAME,
        "message"
    )

    PLACE_ORDER = (
        By.XPATH,
        "//a[contains(text(),'Place Order')]"
    )

    SUCCESS_TEXT = (
        By.XPATH,
        "//*[contains(text(),'Order Placed')]"
    )

    def open_cart(self):

        self.click(self.CART_BUTTON)

    def proceed_checkout(self):

        self.click(self.PROCEED_TO_CHECKOUT)

    def click_register_login(self):

        self.wait.until(
            EC.visibility_of_element_located(
                self.REGISTER_LOGIN
            )
        ).click()

    def add_comment(self, text="Automation Order"):

        self.wait.until(
            EC.visibility_of_element_located(
                self.COMMENT_BOX
            )
        ).send_keys(text)

    def place_order(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.PLACE_ORDER
            )
        ).click()

    def is_order_successful(self):

        try:
            return self.wait.until(
                EC.visibility_of_element_located(
                    self.SUCCESS_TEXT
                )
            ).is_displayed()

        except:
            return False