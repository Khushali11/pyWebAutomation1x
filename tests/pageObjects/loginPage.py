# page class
#page locators
#page actions
#webdriver-init
#customfuction
#no assertion here

from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self,driver):
        self.driver=driver
    #page locators
    username=(By.ID,"login-username")
    password=(By.ID,"login-password")
    submit_button=(By.ID,"js-login-btn")
    error_message=(By.ID,"js-notification-box-msg")
    free_trail=(By.XPATH,"//a[@class='text-link']")

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)
    def get_password(self):
        return self.driver.find_element(*LoginPage.password)
    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)
    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)
    def get_free_trail(self):
        return self.driver.find_element(*LoginPage.free_trail)
    #page action
    def login_to_vwo(self,user,pwd):
        self.get_username().send_keys(user)
        self.get_password().send_keys(pwd)

        self.get_submit_button().click()
    def get_error_message_text(self):
        return self.get_error_message().text

    def  click_free_trail(self):
        self.get_free_trail().click()


