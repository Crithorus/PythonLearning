#   Examples on how to find fields in websites

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)

serviceObj = Service("/Users/timot/Documents/chromedriver")
driver = webdriver.Chrome(options=options, service=serviceObj)

driver.get("https://rahulshettyacademy.com/client")

#   when inspecting a web page '<a' means it has  a link
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

#   we can also use parent, travel through using tags
#   XPath method
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
#   CSS method (use space and nth-child(index)
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("123456")
#driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
#   using text without link <'a
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
