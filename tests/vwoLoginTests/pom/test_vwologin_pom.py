import time
import allure
import pytest

from tests.pageObjects.loginPage import LoginPage
from tests.pageObjects.DashboardPage import DashbordPage
from selenium import webdriver


class TestLogin():

    @allure.epic("VWO Login Test")
    @allure.feature("TC#0 VWO App NegativeTest")
    @pytest.mark.usefixtures("setup")
    def test_vwologin_negative(self, setup):
        driver = setup
        driver.get(self.base_url)
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user="admin", pwd="admin")
        time.sleep(5)
        error_message = loginPage.get_error_message_text()
        assert error_message == "Your email, password, IP address or location did not match"
        time.sleep(5)

    @allure.epic("VWO Login Test")
    @allure.feature("TC#1 VWO App PositiveTest")
    @pytest.mark.usefixtures("setup")
    def test_vwologin_positive(self, setup):
        driver = setup
        driver.get(self.base_url)
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user=self.username, pwd=self.password)
        time.sleep(10)
        assert "Dashboard" in driver.title
        time.sleep(5)

    def tearDown(self):
        pass
