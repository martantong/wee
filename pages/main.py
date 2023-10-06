from selenium.webdriver.common.by import By

from pages.common import CommonPage


class MainPage(CommonPage):
    PROFILE_BTN = (By.XPATH, "//div[@title='Profile']")

    def open_login_form(self):
        self.wait_for(self.PROFILE_BTN).click()
