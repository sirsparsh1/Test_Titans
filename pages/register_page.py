from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class RegisterPage(BasePage):

    # Login page
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")

    # Signup section
    NAME = (By.NAME, "name")
    EMAIL = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP = (By.XPATH, "//button[@data-qa='signup-button']")

    # Account info page
    TITLE_MR = (By.ID, "id_gender1")
    PASSWORD = (By.ID, "password")

    DAYS = (By.ID, "days")
    MONTHS = (By.ID, "months")
    YEARS = (By.ID, "years")

    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    ADDRESS = (By.ID, "address1")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE = (By.ID, "mobile_number")

    CREATE_ACCOUNT = (By.XPATH, "//button[@data-qa='create-account']")

    SUCCESS = (
        By.XPATH,
        "//*[contains(text(),'Account Created!')]"
    )

    # ------------------------
    # OPEN SIGNUP PAGE
    # ------------------------
    def open_signup_page(self):
        self.driver.get("https://automationexercise.com/login")

    # ------------------------
    # REGISTER USER
    # ------------------------
    def register_user(self, name, email, password):

        # Signup section
        self.wait.until(
            EC.visibility_of_element_located(self.NAME)
        ).send_keys(name)

        self.driver.find_element(*self.EMAIL).send_keys(email)

        # FIXED HERE
        self.driver.find_element(*self.SIGNUP).click()

        # Account Information Page
        self.wait.until(
            EC.visibility_of_element_located(self.TITLE_MR)
        ).click()

        self.driver.find_element(*self.PASSWORD).send_keys(password)

        Select(
            self.driver.find_element(*self.DAYS)
        ).select_by_visible_text("1")

        Select(
            self.driver.find_element(*self.MONTHS)
        ).select_by_visible_text("January")

        Select(
            self.driver.find_element(*self.YEARS)
        ).select_by_visible_text("2000")

        self.driver.find_element(*self.FIRST_NAME).send_keys("Shaik")

        self.driver.find_element(*self.LAST_NAME).send_keys("Musharaf")

        self.driver.find_element(*self.ADDRESS).send_keys("Hyderabad")

        self.driver.find_element(*self.STATE).send_keys("Telangana")

        self.driver.find_element(*self.CITY).send_keys("Hyderabad")

        self.driver.find_element(*self.ZIPCODE).send_keys("500001")

        self.driver.find_element(*self.MOBILE).send_keys("9876543210")

        self.driver.find_element(*self.CREATE_ACCOUNT).click()

        # Wait for success message
        self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS)
        )

    # ------------------------
    # VERIFY ACCOUNT CREATED
    # ------------------------
    def verify_account_created(self):

        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.SUCCESS)
            ).is_displayed()

        except:
            return False