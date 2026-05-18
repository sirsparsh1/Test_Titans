from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ContactUsPage(BasePage):

    NAME = (By.NAME, "name")
    EMAIL = (By.NAME, "email")
    MESSAGE = (By.NAME, "message")
    SUBMIT = (By.NAME, "submit")

    # better locator (more stable)
    SUCCESS = (By.XPATH, "//*[contains(text(),'Success!')]")

    def submit_form(self, name, email, msg):

        self._remove_ads()

        self.enter_text(self.NAME, name)
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.MESSAGE, msg)

        self._safe_click(self.SUBMIT)

    def is_success(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS)
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