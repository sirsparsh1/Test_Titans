from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CategoryPage(BasePage):

    WOMEN = (By.XPATH, "//a[text()='Women']")
    MEN = (By.XPATH, "//a[text()='Men']")

    def open_women(self):
        self.click(self.WOMEN)

    def open_men(self):
        self.click(self.MEN)