from utils.driver_factory import DriverFactory
from pages.register_page import RegisterPage
import time
import random


def test_registration():

    driver = DriverFactory.get_driver("chrome")
    driver.get("https://automationexercise.com")

    register = RegisterPage(driver)

    register.open_signup_page()

    email = f"test_{random.randint(1000,9999)}@mail.com"

    register.register_user(
        "Test User",
        email,
        "Test@123"
    )

    assert register.verify_account_created()

    driver.quit()