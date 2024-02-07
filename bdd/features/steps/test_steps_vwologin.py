from behave import given, when, then
from selenium.webdriver.common.by import By
import time


@given('open the app.vwo.com')
def step_impl(context):
    pass


@when('I enter the {username} and {password}')
def step_impl(context, username, password):
    print(username, password)


# write a code for login to app.vwo.com
@then('I get this {message}')
def step_impl(context, message):
    print(message)
    # return (expected_response.get(context.greeting, ''))
    # assert expected_response.get(context.greeting, " ") == response

# pip install allure-behave
# behave -f allure_behave.formatter:AllureFormatter -o allure-report C:\Users\Dell\PycharmProjects\pythonProject\pyWebAutomation1x\bdd\features
#allure serve allure-report
 #pip freeze >requirement.txt
