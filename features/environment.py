from utils.driver_factory import DriverFactory
import time


def before_scenario(context, scenario):

    context.driver = DriverFactory.get_driver("chrome")

    context.driver.maximize_window()

    context.driver.get("https://automationexercise.com/")


def after_scenario(context, scenario):

    time.sleep(3)

    context.driver.quit()