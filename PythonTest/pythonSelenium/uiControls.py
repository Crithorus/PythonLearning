from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)

serviceObj = Service("/Users/timot/Documents/chromedriver")
driver = webdriver.Chrome(options=options, service=serviceObj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

cb = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for item in cb:
    if item.get_attribute("value") == "option2":
        item.click()
        #   to check if item is selected/ to ensure it occured
        assert item.is_selected()
        break

#   ====================Assignment radio button
radios = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
#   Do this if position is unknown
for rad in radios:
    if rad.get_attribute("value") == "radio2":
        rad.click()
        break
#   Do this if position is fixed
radios[0].click()
assert radios[0].is_selected()
# ================================================
#   check if item is displayed in the webpage
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
