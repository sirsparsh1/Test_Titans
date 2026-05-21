from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ContactUsPage(BasePage):

    NAME = (By.NAME, "name")
    EMAIL = (By.NAME, "email")
    MESSAGE = (By.NAME, "message")
    SUBMIT = (By.NAME, "submit")

    SUCCESS = (
        By.XPATH,
        "//*[contains(text(),'Success! Your details have been submitted successfully.')]"
    )

    def submit_form(self, name, email, msg):
        self.enter_text(self.NAME, name)
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.MESSAGE, msg)

        self.click(self.SUBMIT)

        # Accept alert popup
        self.driver.switch_to.alert.accept()

    def verify_success(self):
        return self.wait.until(
            lambda d: d.find_element(*self.SUCCESS).is_displayed()
        )