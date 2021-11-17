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

class BulkApothecary():
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
            try:
                d.find_element(By.CSS_SELECTOR, ".sumome-react-wysiwyg-outside-horizontal-resize-handles > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)").click()
                print("Closed the popup")
            except:
                print("There was no popup...")
                pass
                
            d.find_element(By.CSS_SELECTOR, "label.form-label:nth-child(9)").click()
            d.find_element(By.ID, "form-action-addToCart").click()
            time.sleep(1)
            d.get("https://www.bulkapothecary.com/checkout")
            time.sleep(0.5)
            d.find_element(By.ID, "email").send_keys(p['shipping_address']['email'])
            d.find_element(By.ID, "checkout-customer-continue").click()
            time.sleep(0.5)

            d.find_element(By.ID, "firstNameInput").send_keys(p['shipping_address']['first_name'])
            d.find_element(By.ID, "lastNameInput").send_keys(p['shipping_addresss']['last_name'])
            element = d.find_element(By.ID, "countryCodeInput")
            Select(element).select_by_visible_text(p['billing_address']['country'])
            d.find_element(By.ID, "postCodeInput").send_keys(p['shipping_address']['zipcode'])
            d.find_element(By.ID, "cityInput").send_keys(p['shipping_address']['city'])
            d.find_element(By.ID, "addressLine1Input").send_keys(p['shipping_address']['address'])
            d.find_element(By.ID, "addressLine2Input").send_keys(p['shipping_address']['address_2'])






            print("Done")
            time.sleep(5)
            self.stop()
        except Exception as e:
            self.stop()
            raise e

if __name__ == "__main__":
    with open('profile.json') as file:
        profile = json.load(file)
        product_url = "https://www.bulkapothecary.com/product/raw-ingredients/waxes-and-butters/beeswax-white-and-yellow/"
        b = BulkApothecary()
        b.run(product_url, profile)

