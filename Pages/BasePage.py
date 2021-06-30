import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self,driver):
        self.driver = driver

    def enterValue(self,by_locator,value):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(value)

    def getText(self,by_locator):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).text

    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()

    def get_title(self):
        return self.driver.title

    def is_visible(self,by_locator):
        return bool(WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)))