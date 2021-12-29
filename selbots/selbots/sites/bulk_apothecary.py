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
            time.sleep(5) # failed on 1 second
            d.find_element(By.ID, "checkout-customer-continue").click()
            time.sleep(5)

            d.find_element(By.ID, "firstNameInput").send_keys(p['shipping_address']['first_name'])
            d.find_element(By.ID, "lastNameInput").send_keys(p['shipping_address']['last_name'])
            element = d.find_element(By.ID, "countryCodeInput")
            Select(element).select_by_visible_text(p['billing_address']['country'])

            # https://stackoverflow.com/a/44184600/14775744
            elem = d.find_element(By.ID, "postCodeInput")
            elem.send_keys(p['shipping_address']['zipcode'])
            elem.send_keys(Keys.ARROW_DOWN)
            # wait for the first dropdown option to appear and open it
            # first_option = WebDriverWait(d, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#ui-id-307")))
            # first_option.send_keys(Keys.RETURN)
            time.sleep(5)
            elem.send_keys(Keys.RETURN)
            
            element = d.find_element(By.ID, "provinceCodeInput")
            Select(element).select_by_visible_text(p['shipping_address']['state'])
            # d.find_element(By.ID, "cityInput").send_keys(p['shipping_address']['city']) dont need to provide city
            d.find_element(By.ID, "addressLine1Input").send_keys(p['shipping_address']['address'])
            # d.find_element(By.ID, "addressLine2Input").send_keys(p['shipping_address']['address_2']) TODO: have to deal with popup that suspects bad suite #
            d.find_element(By.ID, "companyInput").send_keys(p['shipping_address']['company'])
            d.find_element(By.ID, "phoneInput").send_keys(p['shipping_address']['phone'])
            time.sleep(7)

            d.find_element(By.CSS_SELECTOR, "li.form-checklist-item:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(2)").click()
            time.sleep(5)

            subtotal = d.find_element(By.CSS_SELECTOR, ".cart-priceItem--subtotal > span:nth-child(2) > span:nth-child(1)").text
            shipping = d.find_element(By.CSS_SELECTOR, "section.cart-section:nth-child(3) > div:nth-child(2) > div:nth-child(1) > span:nth-child(2) > span:nth-child(1)").text
            tax = d.find_element(By.CSS_SELECTOR, "section.cart-section:nth-child(3) > div:nth-child(3) > div:nth-child(1) > span:nth-child(2) > span:nth-child(1)").text
            total = d.find_element(By.CSS_SELECTOR, ".cart-priceItem--total > span:nth-child(2) > span:nth-child(1)").text

            print("Subtotal: ", subtotal)
            print("Shipping: ", shipping)
            print("Tax: ", tax)
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
        product_url = "https://www.bulkapothecary.com/product/raw-ingredients/waxes-and-butters/beeswax-white-and-yellow/"
        b = BulkApothecary()
        b.run(product_url, profile)

