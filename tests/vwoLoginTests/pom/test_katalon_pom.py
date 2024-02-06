import time
import allure
import pytest

from tests.pageObjects.KatalonHomePage import KatalongHomePage
from tests.pageObjects.DashboardPage import DashbordPage
from selenium import webdriver


class TestLogin():

    @allure.epic("Katalong home Test")
    @allure.feature("TC#0 Katalong home page")
    @pytest.mark.usefixtures("setup")
    def test_katalon_login(self, setup):
        driver = setup
        driver.get(self.katalon_url)
        khp = KatalongHomePage(driver)
        khp.click_homepage()
        time.sleep(5)
        assert "https://katalon-demo-cura.herokuapp.com/profile.php#login"==driver.current_url
        time.sleep(5)

    def tearDown(self):
        pass
