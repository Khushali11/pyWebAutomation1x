from behave import given, when, then
from selenium.webdriver.common.by import By
import time


@given('we have behave installed')
def step_impl(context):
    pass


@when('we say {greeting}')
def step_impl(context, greeting):
    context.greeting = greeting


@then('behave should respond with {response}')
def step_impl(context, response):
    expected_response = {
        "HELLO     ": "HI,There  ",
        "Goodbye   ": "See you later! ",
        "Thank you ": "you are welcome! "
    }
    #return (expected_response.get(context.greeting, ''))
    assert expected_response.get(context.greeting, " ") == response
