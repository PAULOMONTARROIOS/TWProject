import os
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class MarsHomePage(BasePage):

    departing_select          = (By.ID,    "departing")
    departing_select_options  = (By.XPATH, "//*[@id='departing']//option")
    returning_select          = (By.ID,    "returning")
    returning_select_options  = (By.XPATH, "//*[@id='returning']//option")
    promotional_code_field    = (By.ID,    "promotional_code")
    search_button             = (By.XPATH, "//form[@action='/pauloricardomontarroios']//input[@value='Search']")

    
    def verify_departing_select_exist(self) -> bool:
        return super().find(EC.visibility_of_element_located(self.departing_select)) != None

    
    def verify_returning_select_exist(self) -> bool:
        return super().find(EC.visibility_of_element_located(self.returning_select)) != None

    
    def get_departing_select_options(self) -> list:
        return super().find_elements(EC.presence_of_all_elements_located(self.departing_select_options),self.departing_select_options)[1:]


    def get_returning_select_options(self) -> list:
        return super().find_elements(EC.presence_of_all_elements_located(self.returning_select_options),self.returning_select_options)[1:]


    def select_departing(self, value):
        super().select_in_combo_visible_text(self.departing_select, value)

    
    def select_returning(self, value):
        super().select_in_combo_visible_text(self.returning_select, value)

    
    def type_promotional_code(self,value):
        super().type_in(EC.visibility_of_element_located(self.promotional_code_field), value)


    def click_search_button(self):
        super().click(EC.visibility_of_element_located(self.search_button))