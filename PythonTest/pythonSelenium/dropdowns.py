#   Handling dropdowns
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)

serviceObj = Service("/Users/timot/Documents/chromedriver")
driver = webdriver.Chrome(options=options, service=serviceObj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

#   Get auto-suggest input text-box
driver.find_element(By.CSS_SELECTOR, "#autosuggest").send_keys("ind")
#   implement a sleep function to wait for website to load
sleep(2)
#   finds all css element on the page with the specified selector
#   store all matching items in a variable
countries = driver.find_elements(By.CSS_SELECTOR, "li[class = 'ui-menu-item'] a")
print(len(countries))  # check size of list
#   Iterate through each web element
for country in countries:
    if country.text == "India":
        country.click()
        break
#   .text will only show if its already pre-built into the website
#   to show text that has been input through automation/script, we will need to
#   get_attribute("value")
assert driver.find_element(By.CSS_SELECTOR, "#autosuggest").get_attribute("value") == "ISndia"

