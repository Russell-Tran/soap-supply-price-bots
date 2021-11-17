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

        # self.driver.get("https://www.brambleberry.com/shop-by-product/ingredients/waxes/premium-yellow-beeswax/V001192.html")
        # self.driver.set_window_size(1800, 850)
        
        # timeout = 5
        # try:
        #     # https://stackoverflow.com/a/37303115/14775744
        #     element_present = EC.presence_of_element_located((By.ID, "CybotCookiebotDialogBodyUnderlay"))
        #     WebDriverWait(self.driver, timeout).until(element_present)
        # except TimeoutException:
        #     print("Timed out waiting for page to load")

        # time.sleep(3)
        # # Cookie
        # self.driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
        # time.sleep(3)

        # # Product
        # self.driver.find_element(By.LINK_TEXT, "5 lbs").click()
        # time.sleep(1)

        # self.driver.find_element(By.ID, "add-to-cart").click()

        # # Cart
        # self.driver.get("https://www.brambleberry.com/shoppingbag")
        # time.sleep(2)

        # #self.driver.execute_script("window.scrollTo(0,7)")
        # #self.driver.execute_script("window.scrollTo(0,69)")
        # #element = self.driver.find_element(By.CLASS_NAME, "estimate-shipping")
        # #actions = ActionChains(self.driver)
        # #actions.move_to_element(element).click().perform()

        # # https://stackoverflow.com/a/63157469/14775744
        # # https://stackoverflow.com/questions/41857614/how-to-find-xpath-of-an-element-in-firefox-inspector
        # xpath = "/html/body/div[1]/div[3]/div/div[2]/div[2]/form/div/div[1]/table/tbody/tr[5]/td[1]/table/tbody/tr[1]/td/a"
        # element = self.driver.find_element(By.XPATH, xpath)
        # self.driver.execute_script("arguments[0].click();", element)

        # self.driver.find_element(By.ID, "dwfrm_shippingestimator_shippingestimate_zipcode").click()
        # self.driver.find_element(By.ID, "dwfrm_shippingestimator_shippingestimate_zipcode").send_keys("92673")
        # time.sleep(1)
        # self.driver.find_element(By.NAME, "dwfrm_cart_estimate").click()
        # time.sleep(2)

        # shipping = self.driver.find_element(By.CSS_SELECTOR, ".order-shipping > .align-right").text
        # total = self.driver.find_element(By.CSS_SELECTOR, ".order-value").text

        # print("Shipping ", shipping)
        # print("Total ", total)

        # """
        # self.driver.execute_script("window.scrollTo(0,26)")
        
    
        # self.stop()
        # """

if __name__ == "__main__":
    with open('profile.json') as file:
        profile = json.load(file)
        product_url = "https://www.essentialdepot.com/product/BEESWAX-YELLOW-8LBS.html"
        b = EssentialDepot()
        b.run(product_url, profile)

