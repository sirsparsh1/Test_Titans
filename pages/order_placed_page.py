from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPlacedPage(BasePage):

    SUCCESS_MSG = (By.XPATH, "//*[contains(text(),'Order Placed')]")

    def verify_order(self):
        return self.wait.until(
            lambda d: d.find_element(*self.SUCCESS_MSG).is_displayed()
        )