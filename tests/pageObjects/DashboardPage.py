# page locators
# page actions
from selenium.webdriver.common.by import By


class DashbordPage():
    def __init__(self, driver):
        self.driver = driver
#page locators
    user_logged_in = (By.XPATH, "//span[@data-qa='lufexuloga']")
    #tuple

    def get_user_logged_in(self):
        return self.driver.find_element(*DashbordPage.user_logged_in)
    #unpacking tuple

    def userloggedin_text(self):
        return self.get_user_logged_in().text()
