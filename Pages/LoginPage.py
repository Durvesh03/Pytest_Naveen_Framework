from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class LoginPage(BasePage):
    """By locators - OR"""
    USER = (By.ID, "ctl00_CPHContainer_txtUserLogin")
    PASSWORD = (By.ID, "ctl00_CPHContainer_txtPassword")
    Forgot_pwd_link = (By.LINK_TEXT, "Forgot Password ?")
    LOGIN_BUTTON = (By.ID, "ctl00_CPHContainer_btnLoginn")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self):
        return self.get_title()

    def is_forgot_pwd_exist(self):
        return self.is_visible(self.Forgot_pwd_link)

    def do_login(self, username, password):
        self.do_send_keys(self.USER, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)