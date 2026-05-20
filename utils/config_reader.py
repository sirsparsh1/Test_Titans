import json


class ConfigReader:

    @staticmethod
    def read_config():
        with open("data/config.json", "r") as file:
            return json.load(file)

    @staticmethod
    def get_base_url():
        return ConfigReader.read_config()["base_url"]

    @staticmethod
    def get_browser():
        return ConfigReader.read_config()["browser"]