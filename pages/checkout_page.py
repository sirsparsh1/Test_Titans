from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


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
        By.XPATH,
        "//textarea[@name='message']"
    )

    PLACE_ORDER = (
        By.XPATH,
        "//a[contains(text(),'Place Order')]"
    )

    NAME_ON_CARD = (
        By.NAME,
        "name_on_card"
    )

    CARD_NUMBER = (
        By.NAME,
        "card_number"
    )

    CVC = (
        By.NAME,
        "cvc"
    )

    EXPIRY_MONTH = (
        By.NAME,
        "expiry_month"
    )

    EXPIRY_YEAR = (
        By.NAME,
        "expiry_year"
    )

    PAY_BUTTON = (
        By.ID,
        "submit"
    )

    SUCCESS_TEXT = (
        By.XPATH,
        "//*[contains(text(),'Congratulations')]"
    )

    def open_cart(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.CART_BUTTON
            )
        ).click()

    def proceed_checkout(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.PROCEED_TO_CHECKOUT
            )
        ).click()

    def click_register_login(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.REGISTER_LOGIN
            )
        ).click()

    def add_comment(self, text="Automation Order"):

        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        comment = self.wait.until(
            EC.presence_of_element_located(
                self.COMMENT_BOX
            )
        )

        comment.clear()

        comment.send_keys(text)

    def place_order(self):

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.PLACE_ORDER
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def enter_payment_details(self):

        # Remove ads and overlays
        self.driver.execute_script("""
            document.querySelectorAll('iframe').forEach(
                e => e.remove()
            );

            document.querySelectorAll('.grippy-host').forEach(
                e => e.remove()
            );
        """)

        # Fill payment form
        self.wait.until(
            EC.visibility_of_element_located(
                self.NAME_ON_CARD
            )
        ).send_keys("Musharaf")

        self.driver.find_element(
            *self.CARD_NUMBER
        ).send_keys("4111111111111111")

        self.driver.find_element(
            *self.CVC
        ).send_keys("123")

        self.driver.find_element(
            *self.EXPIRY_MONTH
        ).send_keys("12")

        self.driver.find_element(
            *self.EXPIRY_YEAR
        ).send_keys("2030")

        pay_btn = self.wait.until(
            EC.presence_of_element_located(
                self.PAY_BUTTON
            )
        )

        # Scroll properly
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            pay_btn
        )

        time.sleep(2)

        # Click Pay button using JavaScript
        self.driver.execute_script(
            "arguments[0].click();",
            pay_btn
        )

        # Wait for success redirect
        self.wait.until(
            EC.url_contains("payment_done")
        )

    def is_order_successful(self):

        try:

            current_url = self.driver.current_url

            print("CURRENT URL:", current_url)

            return "payment_done" in current_url

        except Exception as e:

            print("ORDER SUCCESS ERROR:", e)

            return False