import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    USER = (By.ID,"ctl00_CPHContainer_txtUserLogin")
    PASSWORD = (By.ID, "ctl00_CPHContainer_txtPassword")
    LOGIN_BUTTON = (By.ID, "ctl00_CPHContainer_btnLoginn")
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def do_login(self,username,password):
        self.enterValue(self.USER,username)
        self.enterValue(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

    def get_page_title(self):
        return self.get_title()

