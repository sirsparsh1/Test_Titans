from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class BasePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            20
        )

    def click(self, locator):

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def enter_text(self, locator, text):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()

        element.send_keys(text)

    def get_text(self, locator):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        return element.text

    def wait_for_page_load(self):

        self.wait.until(
            lambda d: d.execute_script(
                "return document.readyState"
            ) == "complete"
        )

    def is_visible(self, locator):

        try:

            return self.wait.until(
                EC.visibility_of_element_located(locator)
            ).is_displayed()

        except TimeoutException:

            return False

    def sleep(self, seconds=2):

        time.sleep(seconds)

    def remove_ads(self):

        self.driver.execute_script("""
            document.querySelectorAll('iframe').forEach(
                e => e.remove()
            );
        """)