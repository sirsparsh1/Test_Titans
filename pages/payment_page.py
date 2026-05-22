from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PaymentPage(BasePage):

    NAME_ON_CARD = (By.NAME, "name_on_card")
    CARD_NUMBER = (By.NAME, "card_number")
    PAY_BTN = (By.ID, "submit")

    def enter_payment_details(self, name, card):
        self.enter_text(self.NAME_ON_CARD, name)
        self.enter_text(self.CARD_NUMBER, card)

    def pay(self):
        self.click(self.PAY_BTN)