import os
import sys
import time
import re

from time import sleep

from random import randrange
from hamcrest import assert_that, is_
from selenium.webdriver.support import expected_conditions as EC

from pages.mars_home_page import MarsHomePage
from pages.mars_search_results_page import MarsSearchResultsPage


@given(u'the user accesses the MarsAir website')
def step_impl(context):
    context.page_object = MarsHomePage(context.driver)
    context.driver.get(context.url)


@then(u'the search form presents the standard fields')
def step_impl(context):
    validation = False
    if (context.page_object.verify_departing_select_exist and 
        context.page_object.verify_returning_select_exist):
      validation = True

    assert_that(validation, is_(True))


@when(u'selecting the departure and return that has a seat available')
def step_impl(context):
    context.page_object.select_departing(context.departing_option_with_seats_available)
    context.page_object.select_returning(context.returning_option_with_seats_available)
    context.page_object.click_search_button()


@when(u'selecting the departure and return that does not have a seat available')
def step_impl(context):
    context.page_object.select_departing(context.departing_option_with_no_seats_available)
    context.page_object.select_returning(context.returning_option_with_no_seats_available)
    context.page_object.click_search_button()


@when(u'selecting the departure, return and inform a valid promotional code')
def step_impl(context):
    context.page_object.select_departing(context.departing_option_with_seats_available)
    context.page_object.select_returning(context.returning_option_with_seats_available)
    context.page_object.type_promotional_code(context.valid_promotional_code)
    context.page_object.click_search_button()


@when(u'selecting the departure, returning and entering an invalid promotional code')
def step_impl(context):
    context.page_object.select_departing(context.departing_option_with_seats_available)
    context.page_object.select_returning(context.returning_option_with_seats_available)
    context.page_object.type_promotional_code(context.invalid_promotional_code)
    context.page_object.click_search_button()



@when(u'selecting departure and return less than 1 year apart')
def step_impl(context):
    context.page_object.select_departing(context.departing_option_with_less_than_one_year)
    context.page_object.select_returning(context.returning_option_with_less_than_one_year)
    context.page_object.click_search_button()


@then(u'the user will be redirected to the home page')
def step_impl(context):
    context.execute_steps('''
                        Given the user accesses the MarsAir website
                        Then the search form presents the standard fields
                        And  the options available will only be July and December until the next 2 years
    ''')


@then(u'the options available will only be July and December until the next 2 years')
def step_impl(context):
    validation = True
    for option in context.page_object.get_departing_select_options():
        if(option.text not in context.option_book):
            validation = False

    for option in context.page_object.get_returning_select_options():
        if(option.text not in context.option_book):
            validation = False      

    assert_that(validation, is_(True))