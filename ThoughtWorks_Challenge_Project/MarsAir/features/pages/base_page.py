from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class BasePage:


    def __init__(self, driver):
        self.driver = driver


    def wait_for(self, condition, seconds=30):
        return WebDriverWait(self.driver, seconds).until(condition)

    
    def find(self, condition):
        return self.wait_for(condition)

    
    def find_elements(self, ec, locator):
        self.wait_for(ec)
        return self.driver.find_elements(*locator)


    def click(self, ec):
        self.wait_for(ec).click()


    def type_in(self, ec, text, set_clear=True, set_enter=False):
        element= self.find(ec)
        if set_clear:
            element.clear()
        if set_enter:
            element.send_keys(text, Keys.ENTER)
        else:
            element.send_keys(text)


    def select_in_combo_visible_text(self, locator, value):
        Select(self.wait_for(EC.visibility_of_element_located(locator))).select_by_visible_text(value)


    def wait(self, time):
        sleep(time)