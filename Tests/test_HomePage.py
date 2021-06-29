import time

from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_BaseClass import BaseTest


class Test_Home_Page(BaseTest):
    def test_home_page_title(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = homepage.get_title()
        assert title == TestData.HOME_PAGE_TITLE

    def test_header_value(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        header_val = homepage.get_header_text()
        assert header_val == TestData.HEADER_VAL

    def test_account_name_value(self):
        self.loginpage = LoginPage(self.driver)
        homepage =self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        account_name_val = homepage.get_account_name()
        assert account_name_val == TestData.ACCOUNT_NAME

    def test_student_icon_exist(self):
        self.loginpage = LoginPage(self.driver)
        homepage =self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        flag = homepage.is_student_icon_exist()
        assert flag

    def test_logout(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        homepage.do_logout()
        time.sleep(5)


