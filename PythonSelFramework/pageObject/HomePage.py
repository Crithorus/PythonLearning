#   This exemplifies Page object Design pattern mainly for
#   Modularity and reusability, abstraction of ui details, code readability and easy maintenance

from selenium.webdriver.common.by import By

from pageObject.CheckoutPage import CheckoutPage


class HomePage:
    #   declare page object
    shop = (By.LINK_TEXT, "Shop")

    #   Constructor
    def __init__(self, driver):
        self.driver = driver

    def shopitems(self):
        self.driver.find_element(*HomePage.shop).click()
        #   identify trigger points between pages and use it
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage
