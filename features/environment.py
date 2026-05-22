from utils.driver_factory import DriverFactory
from utils.config_reader import ConfigReader


def before_scenario(context, scenario):

    browser = ConfigReader.get_browser()

    context.driver = DriverFactory.get_driver(
        browser
    )

    context.driver.get(
        ConfigReader.get_base_url()
    )


def after_scenario(context, scenario):

    if hasattr(context, "driver"):
        context.driver.quit()