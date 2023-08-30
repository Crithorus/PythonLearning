from time import sleep

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


driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.implicitly_wait(5)

driver.find_element(By.CLASS_NAME, "blinkingText").click()

windowList = driver.window_handles

driver.switch_to.window(windowList[1])

user = driver.find_element(By.CSS_SELECTOR,"a[href='mailto:mentor@rahulshettyacademy.com']").text

#user = user.replace("mentor@", "").replace(".com", "")
driver.close()
driver.switch_to.window(windowList[0])

#   add items into the fields
password = "learning"

driver.find_element(By.CSS_SELECTOR, "#username").send_keys(user)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "#terms").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
sleep(3)
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
#   print error message
print(driver.find_element(By.XPATH, "//div[@class='alert alert-danger col-md-12']").text)






