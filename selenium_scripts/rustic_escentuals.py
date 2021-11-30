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

class RusticEscentuals():
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
            time.sleep(3)
            d.find_elements(By.ID, "ProductPriceIDText")[1].click()
            time.sleep(20)
            d.find_element(By.ID, "MainContent_ChildContent_ParentData_btnAddToCart_0").click()
            """
            print("C")
            time.sleep(30)
            d.get(shopping_cart_url)
            print("D")
            time.sleep(10)
            d.find_element(By.ID, "MainContent_btnCheckoutGuest").click()
            print("E")
            time.sleep(10)
            d.find_element(By.ID, "MainContent_txtBillFirstNameNew").send_keys(p['shipping_address']['first_name'])
            d.find_element(By.ID, "MainContent_txtBillLastNameNew").send_keys(p['shipping_address']['last_name'])
            d.find_element(By.ID, "MainContent_txtBillAddr1New").send_keys(p['shipping_address']['address'])
            d.find_element(By.ID, "MainContent_txtBillAddr2New").send_keys(p['shipping_address']['address_2'])
            d.find_element(By.ID, "MainContent_txtBillCityNew").send_keys(p['shipping_address']['city'])
            e = d.find_element(By.ID, "MainContent_cmbBillStateProvinceNew")
            Select(e).select_by_visible_text(p['shipping_address']['state'])
            d.find_element(By.ID, "MainContent_txtBillPostalCodeNew").send_keys(p['shipping_addresss']['zipcode'])
            d.find_element(By.ID, "MainContent_txtBillEmailNew").send_keys(p['shipping_addresss']['email'])
            d.find_element(By.ID, "MainContent_txtBillPhoneNew").send_keys(p['shipping_addresss']['phone'])
            d.find_element(By.ID, "MainContent_chkShipToBilling").click()
            time.sleep(1)
            d.find_element(By.ID, "MainContent_btnUpdateBillingShippingNew").click()
            time.sleep(1)

            subtotal = d.find_element(By.ID, "MainContent_lblSubTotal").text
            shipping = d.find_element(By.ID, "MainContent_lblShipCost").text
            coupons = d.find_element(By.ID, "MainContent_lblDiscount").text
            tax = d.find_element(By.ID, "MainContent_lblTaxAmount").text
            total = d.find_element(By.ID, "MainContent_lblGrandTotal").text

            print("Subtotal: ", subtotal)
            print("Shipping: ", shipping)
            print("Tax: ", tax)
            print("Total: ", total)
            print("Done")
            time.sleep(5)
            
            self.stop()
            """
        except Exception as e:
            self.stop()
            raise e

if __name__ == "__main__":
    with open('profile.json') as file:
        profile = json.load(file)
        product_url = "https://www.rusticescentuals.com/products/White-Beeswax-Pastilles-16-ounces.aspx"
        shopping_cart_url = "https://www.rusticescentuals.com/shoppingcart.aspx"
        b = RusticEscentuals()
        b.run(product_url, shopping_cart_url, profile)

