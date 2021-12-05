"""
Zap Sourcing 2021
"""
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# great imports!
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ChemistryStore():
    def start(self):
        self.driver = webdriver.Firefox()

    def stop(self):
        self.driver.stop_client() # This needs to be added in order to close the window
        self.driver.quit()

    def run(self, product_url, shopping_cart_url, profile):
        self.start()
        d = self.driver
        p = profile
        
        try:
            # Required minimum $10 so had to go with 2lb option
            d.get(product_url)
            time.sleep(3)
            d.find_element(By.CSS_SELECTOR, "div.mt10:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(3)").click()
            d.find_element(By.ID, "submit-product-w-options").click()
            time.sleep(5)
            d.get(shopping_cart_url)
            d.find_element(By.ID, "return_login").click()


            # print("Subtotal: ", subtotal)
            # print("Shipping: ", shipping)
            # print("Total: ", total)
            # print("Done")
            # time.sleep(5)
            # self.stop()

        except Exception as e:
            self.stop()
            raise e

if __name__ == "__main__":
    with open('profile.json') as file:
        profile = json.load(file)
        product_url = "https://www.chemistrystore.com/Cosmetic_Waxes-Natural_Yellow_Beeswax.html"
        shopping_cart_url = "https://www.chemistrystore.com/viewcart.cgi#checkoutformlink"
        b = ChemistryStore()
        b.run(product_url, shopping_cart_url, profile)

