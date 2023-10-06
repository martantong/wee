from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class CommonPage:

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 16)
        self._action = ActionChains(self.driver)

    def wait_for(self, locator):
        return self._wait.until(ec.presence_of_element_located(locator))

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click(self, element):
        return self._action.click(element)
