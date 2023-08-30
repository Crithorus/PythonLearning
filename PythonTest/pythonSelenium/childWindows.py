#   This exercise explains how to handle child window from clicks in selenium
#   Reminder: The scope of a Selenium web driver is only on the same tab
#   By default, selenium will have no knowledge of the new tab and therefore needs
#   to be explicitly told  to switch to the child window
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)

serviceObj = Service("/Users/timot/Documents/chromedriver")
driver = webdriver.Chrome(options=options, service=serviceObj)

driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()

#   get window names that are open and put it in a list
windowList = driver.window_handles
#   tell driver to switch child window
driver.switch_to.window(windowList[1])

print(driver.find_element(By.TAG_NAME, "h3").text)
#   close the child tab
driver.close()
#   switch back to parent
driver.switch_to.window(windowList[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text