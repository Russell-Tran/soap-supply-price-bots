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
            # TODO: profile should have boolean commercial address
            d.get(product_url)
            time.sleep(3)
            d.find_element(By.CSS_SELECTOR, "div.mt10:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(3)").click()
            d.find_element(By.ID, "submit-product-w-options").click()
            time.sleep(5)
            d.get(shopping_cart_url)
            d.find_element(By.ID, "return_login").click()
            element = d.find_element(By.CSS_SELECTOR, ".customer-account > ol:nth-child(2) > li:nth-child(1) > select:nth-child(2)")
            Select(element).select_by_visible_text("Corporation")
            d.find_element(By.ID, "email").send_keys(p['shipping_address']['email'])
            time.sleep(3)
            element = d.find_element(By.CSS_SELECTOR, ".billing-address > ol:nth-child(2) > li:nth-child(1) > input:nth-child(2)")
            element.send_keys(p['shipping_address']['first_name'])
            d.find_element(By.CSS_SELECTOR, ".billing-address > ol:nth-child(2) > li:nth-child(2) > input:nth-child(2)").send_keys(p['shipping_address']['last_name'])
            d.find_element(By.CSS_SELECTOR, ".billing-address > ol:nth-child(2) > li:nth-child(3) > input:nth-child(2)").send_keys(p['shipping_address']['company'])
            d.find_element(By.CSS_SELECTOR, ".billing-address > ol:nth-child(2) > li:nth-child(4) > input:nth-child(2)").send_keys(p['shipping_address']['address'])
            d.find_element(By.CSS_SELECTOR, ".billing-address > ol:nth-child(2) > li:nth-child(6) > input:nth-child(2)").send_keys(p['shipping_address']['city'])
            element = d.find_element(By.ID, "country")
            Select(element).select_by_visible_text(p['shipping_address']['country'])
            element = d.find_element(By.CSS_SELECTOR, "#country_fields > li:nth-child(1) > select:nth-child(2)")
            Select(element).select_by_visible_text(p['shipping_address']['state'])
            d.find_element(By.CSS_SELECTOR, "#country_fields > li:nth-child(2) > input:nth-child(2)").send_keys(p['shipping_address']['zipcode'])

            # Is this a commercial address? Clicking by default rn
            # (Notice: move_to_element required to be able to click the checkbox)
            element = d.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/form/div[1]/div[5]/fieldset/ol/li[8]/div/label/input")
            actions = ActionChains(d)
            actions.move_to_element(element).perform()
            element.click()

            d.find_element(By.CSS_SELECTOR, ".billing-address > ol:nth-child(2) > li:nth-child(10) > input:nth-child(2)").send_keys(p['shipping_address']['phone'])
            d.find_element(By.CSS_SELECTOR, ".billing-address > ol:nth-child(2) > li:nth-child(11) > input:nth-child(2)").send_keys(p['shipping_address']['phone'])
            d.find_element(By.ID, "calculate_button").click()

            time.sleep(7)
            d.find_element(By.CSS_SELECTOR, "#shipping_data > ol:nth-child(6) > li:nth-child(4) > input:nth-child(1)").click()

            subtotal = d.find_element(By.CSS_SELECTOR, ".subtotal > span:nth-child(1)").text
            subtotal = re.search('\$[0-9.]+', subtotal).group()   # Returns '$249.99'
            shipping = d.find_element(By.ID, "ShippingCost").text
            tax = d.find_element(By.ID, "taxid").text
            total = d.find_element(By.ID, "Total").text


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
        product_url = "https://www.chemistrystore.com/Cosmetic_Waxes-Natural_Yellow_Beeswax.html"
        shopping_cart_url = "https://www.chemistrystore.com/viewcart.cgi#checkoutformlink"
        b = ChemistryStore()
        b.run(product_url, shopping_cart_url, profile)

