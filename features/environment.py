from utils.driver_factory import DriverFactory
from utils.config_reader import ConfigReader
import time


def before_scenario(context, scenario):

   
    browser = ConfigReader.get_browser()

   
    context.driver = DriverFactory.get_driver(browser)

    
    context.driver.maximize_window()

  
    context.driver.get(
        ConfigReader.get_base_url()
    )


def after_scenario(context, scenario):

    time.sleep(3)

    context.driver.quit()