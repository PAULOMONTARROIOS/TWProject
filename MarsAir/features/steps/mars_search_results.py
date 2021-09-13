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


@given(u'the user is on the search results screen')
def step_impl(context):
    context.page_object = MarsSearchResultsPage(context.driver)


@when(u'click on the MarsAir logo')
def step_impl(context):
    MarsSearchResultsPage(context.driver).click_mars_air_logo()


@then(u'the application should display the friendly message stating that the schedule is unavailable')
def step_impl(context):
    context.page_object = MarsSearchResultsPage(context.driver)
    validation = False
    if(context.message_unvailability_seats_less_than_one_year in context.page_object.get_search_result_message()):
        validation = True

    assert_that(validation, is_(True))


@then(u'the valid promotional code has the correct verifier digit')
def step_impl(context):
    context.page_object = MarsSearchResultsPage(context.driver)
    sum_other_digits = int(context.page_object.get_promo_code()[2]) + int(context.page_object.get_promo_code()[8]) + \
                        int(context.page_object.get_promo_code()[9])

    assert_that(sum_other_digits, is_(int(context.page_object.get_promo_code()[10])))


@then(u'the valid promotional code has the format in the correct pattern')
def step_impl(context):
    context.page_object = MarsSearchResultsPage(context.driver)
    validation = False
    if(re.match('^[A-Z]{2}[0-9]-[A-Z]{3}-[0-9]{3}$', context.page_object.get_promo_code()) != None):
        validation = True

    assert_that(validation, is_(True))


@then(u'the application will display a message stating that the promotional code is invalid')
def step_impl(context):
    context.page_object = MarsSearchResultsPage(context.driver)
    formated_message = context.invalid_promotional_code_message.format(context.invalid_promotional_code)

    assert_that(formated_message, is_(context.page_object.get_promotional_code_message()))


@then(u'the application will display a message describing the promotional code')
def step_impl(context):
    context.page_object = MarsSearchResultsPage(context.driver)
    discount = context.valid_promotional_code[2] + '0%'
    formated_message = context.valid_promotional_code_message.format(context.valid_promotional_code, discount)

    assert_that(formated_message, is_(context.page_object.get_promotional_code_message()))


@then(u'the application of the discount is in accordance with the promotional code')
def step_impl(context):
    context.page_object = MarsSearchResultsPage(context.driver)
    validation = False
    discount = context.valid_promotional_code[2] + '0'

    if discount in context.page_object.get_discount():
        validation = True

    assert_that(validation, is_(True))


@then(u'the application should display a friendly message stating unavailability')
def step_impl(context):
    validation = False
    context.page_object = MarsSearchResultsPage(context.driver)
    if(context.message_stating_unvailability_seats in context.page_object.get_search_result_message()):
        validation = True

    assert_that(validation, is_(True))


@then(u'the application should display the message stating availability')
def step_impl(context):
    validation = False
    context.page_object = MarsSearchResultsPage(context.driver)
    if(context.message_stating_availability_seats in context.page_object.get_search_result_message()):
        validation = True

    assert_that(validation, is_(True))
