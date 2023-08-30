from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_experimental_option('detach', True)

serviceObj = Service("/Users/timot/Documents/chromedriver")
driver = webdriver.Chrome(options=options, service=serviceObj)


driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# #   get veggies list from table
# defaultList = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(1)")
# orig = []
# for item in defaultList:
#     orig.append(item.text)
#
#
# #   sort the original list
# orig.sort(reverse=False)
# print(orig)
driver.find_element(By.CSS_SELECTOR, "tr th:nth-child(1) ").click()
webSort = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(1)")
webSort1 = []
webSort2 = []
for item in webSort:
    webSort1.append(item.text)
    webSort2.append(item.text)

#   Copying list can also be done by
#   webSort2 = webSort1.copy() << this is faster than .slice
webSort1.sort()


assert webSort2 == webSort1
