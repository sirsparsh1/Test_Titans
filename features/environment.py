from utils.driver_factory import DriverFactory
import time


def dismiss_ads(driver):
    """Remove ad iframes and overlays that block test elements."""
    try:
        driver.execute_script("""
            // Remove all ad iframes
            document.querySelectorAll('iframe[id^="aswift_"], iframe[id^="google_ads_"], ins.adsbygoogle, .adsbygoogle').forEach(el => el.remove());
            // Remove any overlay divs from ads
            document.querySelectorAll('div[id^="google_ads_"], div[class*="ad-"]').forEach(el => el.remove());
        """)
    except:
        pass


def before_scenario(context, scenario):

    context.driver = DriverFactory.get_driver("chrome")

    context.driver.maximize_window()

    context.driver.get("https://automationexercise.com/")

    # Wait for page to load then dismiss ads
    time.sleep(2)
    dismiss_ads(context.driver)


def after_scenario(context, scenario):

    time.sleep(3)

    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()