from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    EMAIL = (By.XPATH, "//input[@data-qa='login-email']")
    PASSWORD = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    LOGGED_IN = (By.XPATH, "//*[contains(text(),'Logged in as')]")

    def open_login_page(self):
        self.wait_for_page_load()
        self.click(self.LOGIN_LINK)
        self.wait_for_page_load()

    def enter_email(self, email):
        self.enter_text(self.EMAIL, email)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
        self.wait_for_page_load()

    def verify_login(self):
        try:
            element = self.wait.until(
            EC.visibility_of_element_located(self.LOGGED_IN)
            )
            return element.is_displayed()
        except Exception:
            return False
        
    def is_logged_in(self):
        return len(self.driver.find_elements(*self.LOGGED_IN)) > 0