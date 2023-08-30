from time import sleep
#   IMPORTANT
#   For CSS_SELECTOR, '.' is for class and # is for ID
#   This is an example of functional testing
#   Teaches how to do implicit/explicit waits
#   It is important as websites can take time to load or actions have wait times
#   IMPLICIT WAIT: a global timeout on top of scripts
#   EXPLICIT WAIT: applies to the specified element/object
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

#   IMPLICIT IMPL
#   5 seconds is max time out. If element shows in 2 seconds, save 3 seconds
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
sleep(2)
#   A special case where implicit waits dont work as list can return empty
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0

#   Assignment 2
fromWeb = []
myList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']

for result in results:
    #   An example of chaining the web elements(from parent to child)
    result.find_element(By.XPATH, "div/button").click()
    fromWeb.append(result.find_element(By.XPATH, "h4").text)

driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()

driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#   Explicit wait is a wait for a specific object and overrides implicit wait
wait = WebDriverWait(driver, 10)  # specify which driver and duration
wait.until(expected_conditions.presence_of_element_located(
    (By.CLASS_NAME, "promoInfo")))  # wait until it is visible/present on webpage

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

totals = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
cartSum = 0
for itm in totals:
    cartSum += int(itm.text)

print(cartSum)

webAmt = driver.find_element(By.CSS_SELECTOR, ".totAmt").text

assert int(webAmt) == cartSum

#   ===================ASSIGNMENT 1=====================
disc = float(driver.find_element(By.CSS_SELECTOR, ".discountPerc").text.rstrip("%")) / 100
discPrice = float(webAmt) * (1 - disc)
assert discPrice < float(webAmt)


#   ===================ASSIGNMENT 2======================
assert myList == fromWeb