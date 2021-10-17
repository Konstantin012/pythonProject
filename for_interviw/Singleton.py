from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



class WebDriver:

    class __WebDriver:
        def __init__(self):
            servise = Service("for_interviw/chromedriver.exe")
            self.driver = webdriver.Chrome(service=servise)

    driver = None

    def __init__(self):
        if not self.driver:
            WebDriver.driver = WebDriver.__WebDriver().driver



def website_opener():
    d = WebDriver().driver
    # driver.get('https://google.com')
    driver2 = WebDriver().driver


website_opener()
