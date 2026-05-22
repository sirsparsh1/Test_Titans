from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountPage(BasePage):

    DELETE_ACCOUNT = (By.XPATH, "//a[text()='Delete Account']")

    def delete_account(self):
        self.click(self.DELETE_ACCOUNT)