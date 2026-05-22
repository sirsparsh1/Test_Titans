from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from pages.base_page import BasePage


class ContactUsPage(BasePage):

    CONTACT_US_LINK = (
        By.XPATH,
        "//a[contains(text(),'Contact us')]"
    )

    NAME = (
        By.NAME,
        "name"
    )

    EMAIL = (
        By.NAME,
        "email"
    )

    SUBJECT = (
        By.NAME,
        "subject"
    )

    MESSAGE = (
        By.ID,
        "message"
    )

    SUBMIT = (
        By.NAME,
        "submit"
    )

    SUCCESS = (
        By.XPATH,
        "//*[contains(text(),'Success! Your details have been submitted successfully.')]"
    )

    def open_contact_page(self):

        self.driver.get(
            "https://automationexercise.com/contact_us"
        )

    def submit_form(
            self,
            name,
            email,
            subject,
            message
    ):

        # Remove ads / iframe overlays
        self._remove_ads()

        # Enter form data
        self.enter_text(
            self.NAME,
            name
        )

        self.enter_text(
            self.EMAIL,
            email
        )

        self.enter_text(
            self.SUBJECT,
            subject
        )

        self.enter_text(
            self.MESSAGE,
            message
        )

        # Click submit safely
        self._safe_click(
            self.SUBMIT
        )

        # Handle popup alert
        try:

            alert = self.wait.until(
                EC.alert_is_present()
            )

            alert.accept()

        except:
            pass

    def is_success(self):

        try:

            return self.wait.until(
                EC.visibility_of_element_located(
                    self.SUCCESS
                )
            ).is_displayed()

        except:
            return False

    def _remove_ads(self):

        self.driver.execute_script("""
            document.querySelectorAll('iframe').forEach(
                e => e.remove()
            );
        """)

    def _safe_click(self, locator):

        element = self.wait.until(
            EC.element_to_be_clickable(
                locator
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )