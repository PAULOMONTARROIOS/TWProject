from selenium import webdriver


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.url = context.config.userdata['app_url']
    context.option_book = context.config.userdata['options_book']
    context.departing_option_with_seats_available = context.config.userdata['departing_option_with_seats_available']
    context.returning_option_with_seats_available = context.config.userdata['returning_option_with_seats_available']
    context.departing_option_with_no_seats_available = context.config.userdata['departing_option_with_no_seats_available']
    context.returning_option_with_no_seats_available = context.config.userdata['returning_option_with_no_seats_available']
    context.departing_option_with_less_than_one_year = context.config.userdata['departing_option_with_less_than_one_year']
    context.returning_option_with_less_than_one_year = context.config.userdata['returning_option_with_less_than_one_year']
    context.message_stating_availability_seats = context.config.userdata['message_stating_availability_seats']
    context.message_stating_unvailability_seats = context.config.userdata['message_stating_unvailability_seats']
    context.message_unvailability_seats_less_than_one_year = context.config.userdata['message_unvailability_seats_less_than_one_year']
    context.valid_promotional_code = context.config.userdata['valid_promotional_code']
    context.invalid_promotional_code = context.config.userdata['invalid_promotional_code']
    context.valid_promotional_code_message = context.config.userdata['valid_promotional_code_message']
    context.invalid_promotional_code_message = context.config.userdata['invalid_promotional_code_message']


def after_scenario(context,scenario):
    context.driver.quit()


def after_step(context, step):
    print(f'Step: {step}`')