from pages.login_page import LoginPage
from utils.driver_factory import DriverFactory


def test_login():

    driver = DriverFactory.get_driver("chrome")

    driver.get("https://automationexercise.com")

    login = LoginPage(driver)

    login.open_login_page()
    login.enter_email("shaikmusharaf863786@gmail.com")
    login.enter_password("Musharaf@786")
    login.click_login()

    assert login.verify_login()

    driver.quit()