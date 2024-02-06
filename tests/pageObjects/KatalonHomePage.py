# page class
#page locators
#page actions
#webdriver-init
#customfuction
#no assertion here

from selenium.webdriver.common.by import By

class KatalongHomePage():

    def __init__(self,driver):
        self.driver=driver
    #page locators
    make_appointment=(By.XPATH, "//a[@id='btn-make-appointment']")

    def get_make_appointment(self):
        return self.driver.find_element(*KatalongHomePage.make_appointment)

    #page action
    def click_homepage(self):
        self.get_make_appointment().click()

