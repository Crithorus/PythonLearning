#   This exercise goes over mouse functionalities such as hover
from time import sleep

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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#   ActionsChains are used for mouse hover/right click/double click
#   actions always end with perform
action = ActionChains(driver)
#   action.click_and_hold()
#   action.double_click(driver.find_element(By...))
#   action.context_click()  #   used if you want to right click on any element
#   action.drag_and_drop()

#   Move cursor to element
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
