#   Examples on how to find fields in websites

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = Options()
options.add_experimental_option('detach', True)

serviceObj = Service("/Users/timot/Documents/chromedriver")
driver = webdriver.Chrome(options=options, service=serviceObj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

#   Locators that selenium supports:
#   ID, Xpath, CSSSelector, Classname, name, linkText
#   To check, go to the website, right-click the field to inspect and see its properties
driver.find_element(By.NAME, "email").send_keys("Test1@gmail.com")

#   With similar identifiers, selenium might get confused as to which element it is identifying
#   It is good to use unique name or ID
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
#   this is a checkbox
driver.find_element(By.ID, "exampleCheck1").click()

#   to X-path for any element : //tagname[@attribute='value'] -> //input[@type='submit']
#   CSS for any element : tagname[attribute='value'] -> input[type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("test1")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()  # Radio Button use HASH #

#   if an element class has spaces, it means that there are more than 1 class
#   capture the text message
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message
#   To select an nth element. Selenium scans from top right
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("2wayBind")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

# ===========================STATIC DROPDOWN
#   Select() needs element of drop down
#   an element is a static dropdown if <select is visible
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)  # choose based on element
dropdown.select_by_visible_text("Female")  # Select by text
