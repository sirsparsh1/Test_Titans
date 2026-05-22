import configparser


class ConfigReader:

    config = configparser.ConfigParser()

    config.read("data/config.ini")

    @classmethod
    def get_browser(cls):
        return cls.config.get(
            "basic info",
            "browser"
        )

    @classmethod
    def get_base_url(cls):
        return cls.config.get(
            "basic info",
            "base_url"
        )