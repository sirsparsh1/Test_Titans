from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):

    PRODUCTS = (By.XPATH, "//a[@href='/products']")
    CONTACT_US_LINK = (By.XPATH, "//a[@href='/contact_us']")

    SUBSCRIPTION_EMAIL = (By.ID, "susbscribe_email")
    SUBSCRIBE_BUTTON = (By.ID, "subscribe")

    SUCCESS_SUBSCRIBE = (
        By.XPATH,
        "//*[contains(text(),'You have been successfully subscribed')]"
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def open_products_page(self):
        self.wait.until(
            EC.element_to_be_clickable(self.PRODUCTS)
        ).click()

    def subscribe_email(self, email):

        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        self.wait.until(
            EC.visibility_of_element_located(self.SUBSCRIPTION_EMAIL)
        ).send_keys(email)

        self.driver.find_element(*self.SUBSCRIBE_BUTTON).click()

    def is_subscription_successful(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_SUBSCRIBE)
        ).is_displayed()