import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.CheckoutPage import CheckoutPage
from utilities.BaseClass import BaseClass
from pageObject.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopitems()

        #   Get all products on the screen
        products = checkoutPage.getCardTitle()
        i = -1
        for product in products:
            i += 1
            productName = product.text
            if productName == "Blackberry":
                checkoutPage.getCardButton()[i].click()

        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        confirmpage = checkoutPage.checkOutItems()

        self.driver.find_element(By.ID, "country").send_keys("ind")

        self.verifyLinkPresence("India")

        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
