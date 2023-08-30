#   some objects are simply embedded on top of html files. Since these
#   are seperate entities, selenium do not have access to them as it only has
#   access to the local html code. We handle this similar to how we handle child windows
#   using driver.switch_to. Look for <iframe tags to check if they exist
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
driver.get("https://the-internet.herokuapp.com/iframe")

#   switch to frames. ID or name can be used
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)
