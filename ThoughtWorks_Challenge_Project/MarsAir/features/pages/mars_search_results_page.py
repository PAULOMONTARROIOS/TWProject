import os
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class MarsSearchResultsPage(BasePage):

    message_search_results   = (By.ID,    "content")
    message_promotional_code = (By.XPATH, "//div[@id='content']/p[@class='promo_code']")
    promo_code               = (By.XPATH, "//div[@id='content']/p[@class='promo_code']//tt")
    discount                 = (By.XPATH, "//div[@id='content']/p[@class='promo_code']//strong")
    mars_air_logo            = (By.XPATH, "//h1//a[@href='/pauloricardomontarroios']")


    def get_search_result_message(self) -> str:
        return super().find(EC.visibility_of_element_located(self.message_search_results)).text

    
    def get_promotional_code_message(self) -> str:
        return super().find(EC.visibility_of_element_located(self.message_promotional_code)).text

    
    def get_promo_code(self) -> str:
        return super().find(EC.visibility_of_element_located(self.promo_code)).text


    def get_discount(self) -> str:
        return super().find(EC.visibility_of_element_located(self.discount)).text


    def click_mars_air_logo(self):
        super().wait(2)
        super().click(EC.visibility_of_element_located(self.mars_air_logo))