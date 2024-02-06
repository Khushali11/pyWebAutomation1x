import os

import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    # driver.maximize_window()

    username = os.getenv("NAME")
    password = os.getenv("PASSWORD")
    base_url = os.getenv("BASE_URL")
    katalon_url = os.getenv("Katalon_URL")
    hr_url=os.getenv("HR_APP_URL")

    #driver.get(base_url)
    request.cls.driver=driver
    request.cls.username = username
    request.cls.password = password
    request.cls.base_url = base_url
    request.cls.katalon_url = katalon_url
    request.cls.hr_url = hr_url

    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def connect_to_excel(request):
    pass

@pytest.fixture(scope="class")
def connect_to_db(request):
    pass

