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

class BulkNaturalOils():
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
            d.get(product_url)
            element = d.find_elements(By.ID, "selectqty")[0]
            Select(element).select_by_visible_text("1")
            d.find_element(By.ID, "product-addtocart-button").click()
            time.sleep(7)
            element = d.find_element(By.CSS_SELECTOR, "div.field:nth-child(4) > div:nth-child(2)").find_element(By.CLASS_NAME, "select")
            Select(element).select_by_visible_text(p['shipping_address']['country'])
            element = d.find_element(By.CSS_SELECTOR, "div.field:nth-child(5) > div:nth-child(2)").find_element(By.CLASS_NAME, "select")
            Select(element).select_by_visible_text(p['shipping_address']['state'])
            element = d.find_element(By.CSS_SELECTOR, "div.field:nth-child(7) > div:nth-child(2)").find_element(By.CLASS_NAME, "input-text")
            element.send_keys(p['shipping_address']['zipcode'])
            time.sleep(5)
            d.find_element(By.ID, "s_method_fedexups_ups_03").click()
            time.sleep(5)
            subtotal = d.find_element(By.CSS_SELECTOR, "tr.totals:nth-child(1) > td:nth-child(2) > span:nth-child(1)").text
            shipping = d.find_element(By.CSS_SELECTOR, "tr.totals:nth-child(2) > td:nth-child(2) > span:nth-child(1)").text
            total = d.find_element(By.CSS_SELECTOR, ".grand > td:nth-child(2) > strong:nth-child(1) > span:nth-child(1)").text

            print("Subtotal: ", subtotal)
            print("Shipping: ", shipping)
            print("Total: ", total)
            print("Done")
            time.sleep(5)
            self.stop()

        except Exception as e:
            self.stop()
            raise e

if __name__ == "__main__":
    with open('profile.json') as file:
        profile = json.load(file)
        product_url = "https://bulknaturaloils.com/beeswax-yellow-granules.html"
        shopping_cart_url = None
        b = BulkNaturalOils()
        b.run(product_url, shopping_cart_url, profile)

