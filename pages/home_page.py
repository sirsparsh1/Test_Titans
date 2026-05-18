from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):

    PRODUCTS = (By.XPATH, "//a[@href='/products']")
    LOGIN = (By.XPATH, "//a[@href='/login']")
    CART = (By.XPATH, "//a[@href='/view_cart']")

    SUBSCRIPTION_EMAIL = (By.ID, "susbscribe_email")
    SUBSCRIBE_BUTTON = (By.ID, "subscribe")

    SUCCESS_SUBSCRIBE = (
        By.XPATH,
        "//*[contains(text(),'You have been successfully subscribed')]"
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 15)   # ✅ increased wait (important)

   

    def open_products_page(self):
        self._remove_ads()  # ✅ IMPORTANT FIX

        element = self.wait.until(
            EC.element_to_be_clickable(self.PRODUCTS)
        )
        self.driver.execute_script("arguments[0].click();", element)  # safer click

    def go_to_login(self):
        self._remove_ads()
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN)
        ).click()

    def go_to_cart(self):
        self._remove_ads()
        self.wait.until(
            EC.element_to_be_clickable(self.CART)
        ).click()

    
    def subscribe_email(self, email):

        self._remove_ads()

        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        self.wait.until(
            EC.visibility_of_element_located(self.SUBSCRIPTION_EMAIL)
        ).send_keys(email)

        self.wait.until(
            EC.element_to_be_clickable(self.SUBSCRIBE_BUTTON)
        ).click()

    def is_subscription_successful(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_SUBSCRIBE)
        ).is_displayed()

    

    def _remove_ads(self):
        """
        Removes iframe ads that block clicks
        """
        self.driver.execute_script("""
            const iframes = document.querySelectorAll('iframe');
            iframes.forEach(frame => frame.remove());
        """)