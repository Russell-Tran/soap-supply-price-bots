# INCOMPLETE!!!
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

class MountainRoseHerbs():
    def start(self):
        self.driver = webdriver.Firefox()

    def stop(self):
        self.driver.stop_client() # This needs to be added in order to close the window
        self.driver.quit()

    def run(self, product_url, profile):
        self.start()
        d = self.driver
        p = profile
        
        try:
            d.get(product_url)
            d.find_element(By.ID, "attribute-2970").click() # The 5 lb option
            d.find_element(By.CSS_SELECTOR, "span.product-quantity-toggle:nth-child(1)").click() # Increase qty from 0 to 1
            d.find_element(By.CSS_SELECTOR, "button.button:nth-child(2) > span:nth-child(1)").click()
            time.sleep(3)
            d.get("https://mountainroseherbs.com/cart.php")
            d.find_element(By.CSS_SELECTOR, "div.right > div:nth-child(3) > span:nth-child(2) > span:nth-child(1)").click()   
            time.sleep(3)
            element = d.find_elements(By.ID, "shipping-state")[1]
            Select(element).select_by_visible_text(p['billing_address']['state'])
            element = d.find_elements(By.ID, "shipping-zip")[1].send_keys(p['billing_address']['zipcode'])
            d.find_element(By.CSS_SELECTOR, "div.right > div:nth-child(3) > div:nth-child(3) > form:nth-child(1) > div:nth-child(4) > button:nth-child(1)").click()

            print("Done")
            time.sleep(5)
            #self.stop()
        except Exception as e:
            #self.stop()
            raise e

if __name__ == "__main__":
    with open('profile.json') as file:
        profile = json.load(file)
        product_url = "https://mountainroseherbs.com/beeswax"
        b = MountainRoseHerbs()
        b.run(product_url, profile)

