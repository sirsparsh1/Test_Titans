from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class DriverFactory:

    @staticmethod
    def get_driver(browser):

        if browser.lower() == "chrome":

            driver = webdriver.Chrome(
                service=Service(
                    ChromeDriverManager().install()
                )
            )

            driver.maximize_window()

            return driver

        raise Exception(
            f"Browser {browser} not supported"
        )