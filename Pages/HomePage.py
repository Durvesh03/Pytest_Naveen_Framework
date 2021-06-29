from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
import pytest

class HomePage(BasePage):
    HEADER = (By.XPATH,"//div[@class='grid_15 welcome_title ']/span")
    ACCOUNT_NAME = (By.ID,"ctl00_headerTopStudent_username")
    STUDENTS_ICON = (By.ID,"ctl00_headerTopStudent_HyperLink1")
    LOGOUT_BUTTON = (By.ID,"ctl00_headerTopStudent_lnkbtnSignout")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_header_text(self):
        return self.get_element_text(self.HEADER)

    def get_account_name(self):
        return self.get_element_text(self.ACCOUNT_NAME)

    def is_student_icon_exist(self):
        return self.is_visible(self.STUDENTS_ICON)

    def do_logout(self):
        self.do_click(self.LOGOUT_BUTTON)