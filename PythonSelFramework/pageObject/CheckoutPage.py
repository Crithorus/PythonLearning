from selenium.webdriver.common.by import By

from pageObject.ConfirmPage import ConfirmPage


class CheckoutPage:
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardButton = (By.CSS_SELECTOR, ".card-footer button")
    checkout = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitle(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardButton(self):
        return self.driver.find_elements(*CheckoutPage.cardButton)

    def checkOutItems(self):
        self.driver.find_element(*CheckoutPage.checkout).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

