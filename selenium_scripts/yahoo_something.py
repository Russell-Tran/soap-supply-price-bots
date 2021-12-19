"""
Note: Tends to break on stock_price_css_selector since e.g. data-reactid='47' changes frequently
on the Yahoo Stocks site.
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
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestYahoosomething():
  def setup_method(self, method):
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless") # https://stackoverflow.com/a/70125885/14775744
    self.driver = webdriver.Firefox(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.stop_client() # This needs to be added in order to close the window
    self.driver.quit()
  
  def test_yahoosomething(self):
    self.driver.get("https://www.yahoo.com/")
    self.driver.set_window_size(1843, 763)
    self.driver.find_element(By.ID, "root_3").click()
    self.driver.find_element(By.ID, "yfin-usr-qry").click()
    self.driver.find_element(By.ID, "yfin-usr-qry").send_keys("tsla")
    self.driver.find_element(By.ID, "yfin-usr-qry").send_keys(Keys.ENTER)
    self.driver.execute_script("window.scrollTo(0,102)")

    stock_price_css_selector = "#quote-header-info > div > div > div > span[data-reactid='47']" # https://stackoverflow.com/a/48458527/14775744
    timeout = 5
    try:
      # https://stackoverflow.com/a/37303115/14775744
      element_present = EC.presence_of_element_located((By.CSS_SELECTOR, stock_price_css_selector))
      WebDriverWait(self.driver, timeout).until(element_present)
    except TimeoutException:
      print("Timed out waiting for page to load")

    price_per_share = self.driver.find_element_by_css_selector(stock_price_css_selector).text
    self.vars["stock_price"] = price_per_share
    print(str(self.vars["stock_price"]))
  
