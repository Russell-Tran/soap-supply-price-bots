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

class ScentSationalSupply():
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
            d.find_element(By.ID, "option6891808").click() # third option, the 1lb option for titanium
            d.find_element(By.CLASS_NAME, "cart").click()
            time.sleep(3)
            d.find_element(By.ID, "cart_checkout1").click()
            time.sleep(3)
            d.find_element(By.ID, "accountFrm_accountguest").click()
            d.find_element(By.CSS_SELECTOR, "button.btn:nth-child(4)").click()

            d.find_element(By.ID, "guestFrm_firstname").send_keys(p['shipping_address']['first_name'])
            d.find_element(By.ID, "guestFrm_lastname").send_keys(p['shipping_address']['last_name'])
            d.find_element(By.ID, "guestFrm_email").send_keys(p['shipping_address']['email'])
            d.find_element(By.ID, "guestFrm_address_1").send_keys(p['shipping_address']['address'])
            d.find_element(By.ID, "guestFrm_city").send_keys(p['shipping_address']['city'])
            element = d.find_element(By.ID, "guestFrm_zone_id")
            Select(element).select_by_visible_text(p['shipping_address']['state'])
            d.find_element(By.ID, "guestFrm_postcode").send_keys(p['shipping_address']['zipcode'])
            element = d.find_element(By.ID, "guestFrm_country_id")
            Select(element).select_by_visible_text(p['shipping_address']['country'])
            d.find_element(By.CSS_SELECTOR, "button.pull-right").click()

            d.find_element(By.ID, "guest_default_weightdefault_weight_1default_weight.default_weight_1").click()
            d.find_element(By.ID, "guest_payment_methoddefault_pp_standart").click()
            d.find_element(By.CSS_SELECTOR, "button.btn:nth-child(2)").click()

            subtotal = d.find_element(By.CSS_SELECTOR, ".sidewidt > table:nth-child(5) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > span:nth-child(1)").text
            shipping = d.find_element(By.CSS_SELECTOR, ".sidewidt > table:nth-child(5) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > span:nth-child(1)").text
            total = d.find_element(By.CSS_SELECTOR, ".sidewidt > table:nth-child(5) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > span:nth-child(1)").text

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
        product_url = "https://scentsationalsupply.com/additives-for-soapmaking/water-soluble-titanium-dioxide"
        shopping_cart_url = None
        b = ScentSationalSupply()
        b.run(product_url, shopping_cart_url, profile)

