from selenium import webdriver
from cfg import chromedriver_path


class WebDriver:
    wd = None

    @classmethod
    def initiate_web_driver(cls, driver="Chrome"):
        if driver == "Chrome":
            cls.wd = webdriver.Chrome(chromedriver_path)
        return cls.wd
