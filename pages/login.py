from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.common import CommonPage


class LoginDialog(CommonPage):
    PROFILE_BTN = (By.XPATH, "//div[@title='Profile']")
    HELLO_MSG = (By.XPATH, "//h1[text()='Hello!']")
    CODE_SELECT = (By.CLASS_NAME, "select-code")
    PHONE_INP = (By.CSS_SELECTOR, ".input-phone input")
    LOGIN_BTN = (By.XPATH, "//button[@class='btn btn--accent justify-center']")
    NICE_TO_MSG = (By.XPATH, "//div[text()='Nice to meet you!']")

    def open_login_form(self):
        self.wait_for(self.PROFILE_BTN).click()

    @property
    def hello_message(self):
        return self.wait_for(self.HELLO_MSG)

    @property
    def nice_to_message(self):
        return self.wait_for(self.NICE_TO_MSG)

    @property
    def login_button(self) -> WebElement:
        return self.wait_for(self.LOGIN_BTN)

    def select_country_code(self, country: str):

        self.wait_for(self.CODE_SELECT).click()
        xpath = f"//div[contains(@id, 'phoneCodes')]//li[contains(., '{country}')]"
        self.wait_for((By.XPATH, xpath)).click()

    def input_phone(self, phone: str):
        self.wait_for(self.PHONE_INP).send_keys(phone)
