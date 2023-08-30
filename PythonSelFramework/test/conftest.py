#   To invoke browser, it should be done through fixture conf file
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


#   In the case that i want to choose the browser in CLI
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: type1 or type2"
    )


#   invoke the browser
@pytest.fixture(scope="class")
def setUp(request):
    #   retrieve command line value
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        serviceObj = Service('Users/timot/Documents/chromedriver.exe')

        driver = webdriver.Chrome(service=serviceObj)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    #   since we are not able to return because of yield, we will use request
    #   sent to request.class.driver
    request.cls.driver = driver

    #   tear down after use
    yield
    driver.close()
