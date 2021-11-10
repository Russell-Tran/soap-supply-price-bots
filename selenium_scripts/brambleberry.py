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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# great imports!
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Brambleberry():
  def start(self):
    self.driver = webdriver.Firefox()

  def stop(self):
    self.driver.stop_client() # This needs to be added in order to close the window
    self.driver.quit()

  def run(self):
    self.start()

    self.driver.get("https://www.brambleberry.com/shop-by-product/ingredients/waxes/premium-yellow-beeswax/V001192.html")
    self.driver.set_window_size(1800, 850)
    
    timeout = 5
    try:
      # https://stackoverflow.com/a/37303115/14775744
      element_present = EC.presence_of_element_located((By.ID, "CybotCookiebotDialogBodyUnderlay"))
      WebDriverWait(self.driver, timeout).until(element_present)
    except TimeoutException:
      print("Timed out waiting for page to load")

    time.sleep(5)
    # Cookie
    self.driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
    time.sleep(10)

    # Product
    self.driver.find_element(By.LINK_TEXT, "5 lbs").click()
    time.sleep(3)

    self.driver.find_element(By.ID, "add-to-cart").click()

    # Cart
    self.driver.get("https://www.brambleberry.com/shoppingbag")
    time.sleep(5)

    #self.driver.execute_script("window.scrollTo(0,7)")
    #self.driver.execute_script("window.scrollTo(0,69)")
    #element = self.driver.find_element(By.CLASS_NAME, "estimate-shipping")
    #actions = ActionChains(self.driver)
    #actions.move_to_element(element).click().perform()

    # https://stackoverflow.com/a/63157469/14775744
    # https://stackoverflow.com/questions/41857614/how-to-find-xpath-of-an-element-in-firefox-inspector
    xpath = "/html/body/div[1]/div[3]/div/div[2]/div[2]/form/div/div[1]/table/tbody/tr[5]/td[1]/table/tbody/tr[1]/td/a"
    element = self.driver.find_element(By.XPATH, xpath)
    self.driver.execute_script("arguments[0].click();", element)

    self.driver.find_element(By.ID, "dwfrm_shippingestimator_shippingestimate_zipcode").click()
    self.driver.find_element(By.ID, "dwfrm_shippingestimator_shippingestimate_zipcode").send_keys("92673")
    time.sleep(1)
    self.driver.find_element(By.NAME, "dwfrm_cart_estimate").click()
    time.sleep(5)

    shipping = self.driver.find_element(By.CSS_SELECTOR, ".order-shipping > .align-right").text
    total = self.driver.find_element(By.CSS_SELECTOR, ".order-value").text

    print("Shipping ", shipping)
    print("Total ", total)

    """
    self.driver.execute_script("window.scrollTo(0,26)")
    
  
    self.stop()
    """

if __name__ == "__main__":
  b = Brambleberry()
  b.run()

