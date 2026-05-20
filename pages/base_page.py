from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, locator):
        # Dismiss any ad overlays before clicking
        try:
            self.driver.execute_script("""
                document.querySelectorAll('iframe[id^="aswift_"], iframe[id^="google_ads_"], ins.adsbygoogle, .adsbygoogle').forEach(el => el.remove());
                document.querySelectorAll('div[id^="google_ads_"], div[class*="ad-"]').forEach(el => el.remove());
            """)
        except:
            pass

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        # Scroll element into view
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def remove_ads(self):
        try:
            self.driver.execute_script("""
                document.querySelectorAll('iframe[id^="aswift_"], iframe[id^="google_ads_"], ins.adsbygoogle').forEach(el => el.remove());
            """)
        except:
            pass

    def enter_text(self, locator, text):
        self.remove_ads()
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def sleep(self, seconds=3):
        time.sleep(seconds)

    def wait_for_page_load(self):
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def get_text(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.text