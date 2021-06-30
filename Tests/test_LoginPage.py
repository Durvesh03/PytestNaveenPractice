import pytest
from selenium import webdriver

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_BaseClass import BaseTest


class Test_login(BaseTest):

    def test_validate_Page_title(self):
        self.lp = LoginPage(self.driver)
        assert self.lp.get_page_title() == TestData.LOGIN_TITLE