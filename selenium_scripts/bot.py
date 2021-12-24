"""
Zap Sourcing 2021
"""
# Used by children classes
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Result():
    def __init__(self):
        self.subtotal = None
        self.shipping = None
        self.tax = None
        self.total = None

class Bot():
    def __init__(self):
        pass

    def start(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless") # https://stackoverflow.com/a/70125885/14775744
        self.driver = webdriver.Firefox(options=options)
        self.driver.set_window_size(1280, 949)

    def stop(self):
        self.driver.stop_client() # This needs to be added in order to close the window
        self.driver.quit()

    """
    p is a dictionary; `profile`
    """
    def run(self, product_url, shopping_cart_url, p):
        pass
        