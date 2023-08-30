#   Examples on how to find fields in websites

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = Options()
options.add_experimental_option('detach', True)
#   headless = No GUI (usually faster for testing
options.add_argument("headless")
#   some websites may have ssl certs which require user to go to advance and proceed anyways
#   to ignore those, add it to options too
options.add_argument("--ignore-certificate-errors")
#   Maximise window before invokeing the website
options.add_argument("--start-maximized")
serviceObj = Service("/Users/timot/Documents/chromedriver")
driver = webdriver.Chrome(options=options, service=serviceObj)

driver.get("https://rahulshettyacademy.com/angularpractice/")