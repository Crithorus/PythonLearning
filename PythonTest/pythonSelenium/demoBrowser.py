from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

#   To prevent web browser from closing automatically after programme finishes executing
options = Options()
options.add_experimental_option('detach', True)

#   selenium cannot directly invoke web browser
#   different web browser requires different drivers
#   gecko for firefox msedge for edge
serviceObj = Service("/Users/timot/Documents/chromedriver")
driver = webdriver.Chrome(options=options, service=serviceObj)

#   maximise window before entering the url
driver.maximize_window()

#   Opening a web browser
driver.get("https://timothytoribio.squarespace.com")
print(driver.title)

print(driver.current_url)

driver.get("https://timothytoribio.squarespace.com/awards")  # To go to another URL
driver.back()  # goes back to prev page
driver.forward()  # goes forward to next page
driver.minimize_window()
