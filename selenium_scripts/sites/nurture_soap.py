"""
Zap Sourcing 2021
"""
import pytest
import time
import json
import re
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

class NurtureSoap():
    def start(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless") # https://stackoverflow.com/a/70125885/14775744
        self.driver = webdriver.Firefox(options=options)

    def stop(self):
        self.driver.stop_client() # This needs to be added in order to close the window
        self.driver.quit()

    def run(self, product_url, shopping_cart_url, profile):
        self.start()
        d = self.driver
        p = profile
        
        try:
            d.get(product_url)
            d.set_window_size(1843, 763) ## << EXPERIMENTAL!!
            d.find_element(By.CSS_SELECTOR, "button.product-form__add-button").click()
            time.sleep(3)
            d.get(shopping_cart_url)
            time.sleep(3)
            d.find_element(By.CSS_SELECTOR, ".cart-recap__checkout").click()
            d.find_element(By.ID, "checkout_email").send_keys(p['shipping_address']['email'])
            d.find_element(By.ID, "checkout_shipping_address_first_name").send_keys(p['shipping_address']['email'])
            d.find_element(By.ID, "checkout_shipping_address_last_name").send_keys(p['shipping_address']['email'])
            d.find_element(By.ID, "checkout_shipping_address_address1").send_keys(p['shipping_address']['email'])
            d.find_element(By.ID, "checkout_shipping_address_city").send_keys(p['shipping_address']['email'])
            element = d.find_element(By.ID, "checkout_shipping_address_country")
            Select(element).select_by_visible_text(p['shipping_address']['country'])
            element = d.find_element(By.ID, "checkout_shipping_address_province")
            Select(element).select_by_visible_text(p['shipping_address']['state'])
            d.find_element(By.ID, "checkout_shipping_address_zip").send_keys(p['shipping_address']['zipcode'])
            d.find_element(By.ID, "checkout_shipping_address_phone").send_keys(p['shipping_address']['phone'])

            d.find_element(By.ID, "continue_button").click()

            time.sleep(5)
            subtotal = d.find_element(By.CSS_SELECTOR, ".total-line--subtotal > td:nth-child(2) > span:nth-child(1)").text
            shipping = d.find_element(By.CSS_SELECTOR, "tr.total-line:nth-child(2) > td:nth-child(2) > span:nth-child(1)").text
            total = d.find_element(By.CSS_SELECTOR, ".payment-due__price").text

            print("Subtotal: ", subtotal)
            print("Shipping: ", shipping)
            print("Total: ", total)
            print("Done")
            time.sleep(5)
            self.stop()

        except Exception as e:
            #self.stop()
            raise e

if __name__ == "__main__":
    with open('profile.json') as file:
        profile = json.load(file)
        product_url = "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/eucalyptus-mint-fragrance-oil-fragrance-oil"
        shopping_cart_url = "https://nurturesoap.com/cart"
        b = NurtureSoap()
        b.run(product_url, shopping_cart_url, profile)

