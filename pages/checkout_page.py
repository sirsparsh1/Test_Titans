from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    CART_LINK = (By.XPATH, "//a[@href='/view_cart']")
    CHECKOUT = (By.XPATH, "//a[contains(text(),'Proceed To Checkout')]")
    PLACE_ORDER = (By.XPATH, "//a[contains(text(),'Place Order')]")

    NAME_ON_CARD = (By.NAME, "name_on_card")
    CARD_NUMBER = (By.NAME, "card_number")
    CVC = (By.NAME, "cvc")
    EXPIRY_MONTH = (By.NAME, "expiry_month")
    EXPIRY_YEAR = (By.NAME, "expiry_year")
    PAY_BUTTON = (By.ID, "submit")

    SUCCESS_MSG = (By.XPATH, "//*[contains(text(),'Congratulations')]")

  

    def open_cart(self):
        self._remove_ads()

        element = self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def place_order(self):
        self.open_cart()

        self._safe_click(self.CHECKOUT)
        self._safe_click(self.PLACE_ORDER)

    def fill_payment_details(self):

        self._remove_ads()

        self.enter_text(self.NAME_ON_CARD, "Test User")
        self.enter_text(self.CARD_NUMBER, "4111111111111111")
        self.enter_text(self.CVC, "123")
        self.enter_text(self.EXPIRY_MONTH, "12")
        self.enter_text(self.EXPIRY_YEAR, "2028")

        self._safe_click(self.PAY_BUTTON)

    def is_order_successful(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MSG)
        ).is_displayed()

   

    def _remove_ads(self):
        self.driver.execute_script("""
            document.querySelectorAll('iframe').forEach(e => e.remove());
        """)

    def _safe_click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)