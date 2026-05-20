from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.base_page import BasePage


class CategoryPage(BasePage):

    WOMEN = (By.XPATH, "//a[@href='#Women']")
    DRESS = (By.XPATH, "//div[@id='Women']//a[contains(@href,'category_products')]")

    def open_women(self):
        self.remove_ads()
        self.driver.execute_script("window.scrollTo(0, 400);")
        women_el = self.driver.find_element(*self.WOMEN)
        self.driver.execute_script("arguments[0].click();", women_el)
        import time
        time.sleep(1)
        dress_el = self.driver.find_element(*self.DRESS)
        self.driver.execute_script("arguments[0].click();", dress_el)