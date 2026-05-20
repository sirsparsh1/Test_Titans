import os


class ScreenshotHelper:

    @staticmethod
    def take_screenshot(driver, scenario_name):

        path = "reports/screenshots"
        os.makedirs(path, exist_ok=True)

        file_path = f"{path}/{scenario_name}.png"
        driver.save_screenshot(file_path)

        return file_path