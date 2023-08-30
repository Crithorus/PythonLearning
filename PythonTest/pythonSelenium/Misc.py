#   This exercise teaches how to execute javascript code using selenium.
#   Handling dropdowns

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)
#   headless = No GUI (usually faster for testing
options.add_argument("headless")
#   some websites may have ssl certs which require user to go to advance and proceed anyways
#   to ignore those, add it to options too
options.add_argument("--ignore-certificate-errors")

serviceObj = Service("/Users/timot/Documents/chromedriver")
driver = webdriver.Chrome(options=options, service=serviceObj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)

#   Execute java script in selenium
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

#   take screenshots
#   driver.get_screenshot_as_file("screen.png")