from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#   set behavior of the browser before invocation
options = Options()
options.add_experimental_option('detach', True)


serviceObj = Service("/Users/timot/Documents/chromedriver")
driver = webdriver.Chrome(options=options, service=serviceObj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Test")
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
#   by default, drivers are not aware of popups
#   we need to inform the driver of this alert
alert = driver.switch_to.alert
print(alert.text)
#   to click on the alert button


assert "Test" in alert.text
alert.accept()  # positive(yes)
# alert.dismiss()  # negative(no)
