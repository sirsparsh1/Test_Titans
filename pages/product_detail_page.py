from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductDetailPage(BasePage):

    ADD_TO_CART = (By.XPATH, "//button[@class='btn btn-default cart']")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)