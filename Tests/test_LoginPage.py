import pytest
import allure
from allure_commons.types import AttachmentType

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_BaseClass import BaseTest

@allure.severity(allure.severity_level.NORMAL)
class Test_Login(BaseTest):
    @allure.severity(allure.severity_level.MINOR)
    def test_forgot_pwd_link_visible(self):
        self.loginpage = LoginPage(self.driver)
        flag = self.loginpage.is_forgot_pwd_exist()
        if flag :
            assert True
        else:
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_page_title(self):
        self.loginpage = LoginPage(self.driver)
        title = self.loginpage.get_login_page_title()
        if title == TestData.LOGIN_PAGE_TITLE:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name = "LoginPage_Title",
                          attachment_type= AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.BLOCKER)
    def test_do_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)

