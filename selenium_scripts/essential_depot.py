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

class EssentialDepot():
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
            d.find_element(By.ID, "js-add-to-cart").click()
            d.find_element(By.ID, "js-mini-basket").click()

            time.sleep(3)
            element = d.find_element(By.XPATH, "/html/body/div[3]/header/div[2]/div[3]/div[1]/div[3]/a")
            d.execute_script("arguments[0].click();", element)

            time.sleep(3)
            d.find_element(By.LINK_TEXT, "Continue as a Guest").click()
            
            time.sleep(3)
            d.find_element(By.ID, "js-billing-to-show").click()

            # Enter shipping info
            d.find_element(By.ID, "l-ShipFirstName").send_keys(p['shipping_address']['first_name'])
            d.find_element(By.ID, "l-ShipLastName").send_keys(p['shipping_address']['last_name'])
            d.find_element(By.ID, "l-ShipEmail").send_keys(p['shipping_address']['email'])
            d.find_element(By.ID, "l-ShipPhone").send_keys(p['shipping_address']['phone'])
            d.find_element(By.ID, "l-ShipFax").send_keys(p['shipping_address']['fax'])
            d.find_element(By.ID, "l-ShipCompany").send_keys(p['shipping_address']['company'])
            d.find_element(By.ID, "l-ShipAddress1").send_keys(p['shipping_address']['address'])
            d.find_element(By.ID, "l-ShipAddress2").send_keys(p['shipping_address']['address_2'])
            d.find_element(By.ID, "l-ShipCity").send_keys(p['shipping_address']['city'])
            element = d.find_element(By.ID, "ShipStateSelect")
            Select(element).select_by_visible_text(p['shipping_address']['state'])
            d.find_element(By.ID, "l-ShipZip").send_keys(p['shipping_address']['zipcode'])
            element = d.find_element(By.ID, "ShipCountry")
            Select(element).select_by_visible_text(p['shipping_address']['country'])

            # Enter billing info
            d.find_element(By.ID, "l-BillFirstName").send_keys(p['billing_address']['first_name'])
            d.find_element(By.ID, "l-BillLastName").send_keys(p['billing_address']['last_name'])
            d.find_element(By.ID, "l-BillEmail").send_keys(p['billing_address']['email'])
            d.find_element(By.ID, "l-BillPhone").send_keys(p['billing_address']['phone'])
            d.find_element(By.ID, "l-BillFax").send_keys(p['billing_address']['fax'])
            d.find_element(By.ID, "l-BillCompany").send_keys(p['billing_address']['company'])
            d.find_element(By.ID, "l-BillAddress1").send_keys(p['billing_address']['address'])
            d.find_element(By.ID, "l-BillAddress2").send_keys(p['billing_address']['address_2'])
            d.find_element(By.ID, "l-BillCity").send_keys(p['billing_address']['city'])
            element = d.find_element(By.ID, "BillStateSelect")
            Select(element).select_by_visible_text(p['billing_address']['state'])
            d.find_element(By.ID, "l-BillZip").send_keys(p['billing_address']['zipcode'])
            element = d.find_element(By.ID, "BillCountry")
            Select(element).select_by_visible_text(p['billing_address']['country'])

            # Continue to shipping
            d.find_element(By.CSS_SELECTOR, "input.bg-red").click()
            subtotal = d.find_element(By.CSS_SELECTOR, "strong.column:nth-child(2)").text
            # Next page
            d.find_element(By.CSS_SELECTOR, "input.button:nth-child(2)").click()
            shipping = d.find_element(By.CSS_SELECTOR, "p.whole:nth-child(2) > span:nth-child(2)").text
            total = d.find_element(By.CSS_SELECTOR, "p.column:nth-child(4) > strong:nth-child(2)").text
            
            print("subtotal: ", subtotal)
            print("shipping: ", shipping)
            print("total: ", total)
            print("Done")
            time.sleep(5)
            self.stop()
        except Exception as e:
            self.stop()
            raise e

if __name__ == "__main__":
    with open('profile.json') as file:
        profile = json.load(file)
        product_url = "https://www.essentialdepot.com/product/BEESWAX-YELLOW-8LBS.html"
        b = EssentialDepot()
        b.run(product_url, profile)

