from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class WebDriver:

    class __WebDriver:
        def __init__(self):
            servise = Service("C:\\Users\\KoS\\PycharmProjects\\pythonProject\\for_interviw\\chromedriver.exe")
            self.driver = webdriver.Chrome(service=servise)

    driver:WebDriver = None

    def __init__(self):
        if not self.driver:
            WebDriver.driver = WebDriver.__WebDriver().driver



def website_opener():
    d = WebDriver().driver
    # driver.get('https://google.com')
    # driver2 = WebDriver().driver
    d.get('https://selenium-python.com/')
    element = d.find_element(By.XPATH, "//h2[text()='Python + Selenium']")
    element.click()
website_opener()
