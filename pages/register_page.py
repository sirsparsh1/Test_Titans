from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
import time


class RegisterPage(BasePage):

    # Login Page
    LOGIN_LINK = (
        By.XPATH,
        "//a[contains(text(),'Signup / Login')]"
    )

    # Signup Section
    NAME = (
        By.NAME,
        "name"
    )

    EMAIL = (
        By.XPATH,
        "//input[@data-qa='signup-email']"
    )

    SIGNUP = (
        By.XPATH,
        "//button[@data-qa='signup-button']"
    )

    # Account Info
    TITLE_MR = (
        By.ID,
        "id_gender1"
    )

    PASSWORD = (
        By.ID,
        "password"
    )

    DAYS = (
        By.ID,
        "days"
    )

    MONTHS = (
        By.ID,
        "months"
    )

    YEARS = (
        By.ID,
        "years"
    )

    FIRST_NAME = (
        By.ID,
        "first_name"
    )

    LAST_NAME = (
        By.ID,
        "last_name"
    )

    ADDRESS = (
        By.ID,
        "address1"
    )

    STATE = (
        By.ID,
        "state"
    )

    CITY = (
        By.ID,
        "city"
    )

    ZIPCODE = (
        By.ID,
        "zipcode"
    )

    MOBILE = (
        By.ID,
        "mobile_number"
    )

    CREATE_ACCOUNT = (
        By.XPATH,
        "//button[@data-qa='create-account']"
    )

    SUCCESS = (
        By.XPATH,
        "//*[contains(text(),'Account Created!')]"
    )

    def open_signup_page(self):

        self.driver.get(
            "https://automationexercise.com/login"
        )

        self.wait_for_page_load()

    def register_user(self, name, email, password):

        self._remove_ads()

        # Signup Section
        self.wait.until(
            EC.visibility_of_element_located(self.NAME)
        ).send_keys(name)

        self.driver.find_element(
            *self.EMAIL
        ).send_keys(email)

        signup_btn = self.wait.until(
            EC.element_to_be_clickable(self.SIGNUP)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            signup_btn
        )

        # Account Information
        self.wait.until(
            EC.visibility_of_element_located(
                self.TITLE_MR
            )
        ).click()

        self.driver.find_element(
            *self.PASSWORD
        ).send_keys(password)

        Select(
            self.driver.find_element(*self.DAYS)
        ).select_by_visible_text("1")

        Select(
            self.driver.find_element(*self.MONTHS)
        ).select_by_visible_text("January")

        Select(
            self.driver.find_element(*self.YEARS)
        ).select_by_visible_text("2000")

        self.driver.find_element(
            *self.FIRST_NAME
        ).send_keys("Shaik")

        self.driver.find_element(
            *self.LAST_NAME
        ).send_keys("Musharaf")

        self.driver.find_element(
            *self.ADDRESS
        ).send_keys("Hyderabad")

        self.driver.find_element(
            *self.STATE
        ).send_keys("Telangana")

        self.driver.find_element(
            *self.CITY
        ).send_keys("Hyderabad")

        self.driver.find_element(
            *self.ZIPCODE
        ).send_keys("500001")

        self.driver.find_element(
            *self.MOBILE
        ).send_keys("9876543210")

        # Remove ads before clicking
        self._remove_ads()

        create_btn = self.wait.until(
            EC.element_to_be_clickable(
                self.CREATE_ACCOUNT
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            create_btn
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            create_btn
        )

        # Wait for success message
        self.wait.until(
            EC.visibility_of_element_located(
                self.SUCCESS
            )
        )

    def verify_account_created(self):

        try:

            return self.wait.until(
                EC.visibility_of_element_located(
                    self.SUCCESS
                )
            ).is_displayed()

        except TimeoutException:

            return False

    def _remove_ads(self):

        self.driver.execute_script("""
            document.querySelectorAll('iframe').forEach(
                e => e.remove()
            );
        """)