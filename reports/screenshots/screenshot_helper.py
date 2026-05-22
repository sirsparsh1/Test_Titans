import os


def take_screenshot(driver, scenario_name):

    path = "reports/screenshots"
    os.makedirs(path, exist_ok=True)

    driver.save_screenshot(f"{path}/{scenario_name}.png")