"""
Zap Sourcing 2021
"""
import time
import typing
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

class Result(typing.NamedTuple):
    subtotal: str
    shipping: str
    tax: str
    total: str

class Bot():
    def __init__(self):
        pass

    def start(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless") # https://stackoverflow.com/a/70125885/14775744
        self.driver = webdriver.Firefox(options=options)

    def stop(self):
        self.driver.stop_client() # This needs to be added in order to close the window
        self.driver.quit()

    """
    p is a dictionary `profile`
    """
    def run(self, product_url, shopping_cart_url, p):
        pass
        