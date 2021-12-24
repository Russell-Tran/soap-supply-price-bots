"""
Zap Sourcing 2021
"""
# Used by children classes
import typing
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

class Profile():
    """
    https://stackoverflow.com/a/6993694/14775744
    """
    def __init__(self, profile_dict):
        self.first_name = None
        self.last_name = None
        self.email = None
        self.phone = None
        self.fax = None
        self.company = None
        self.address = None
        self.address_2 = None
        self.city = None
        self.state = None
        self.country = None
        self.zipcode = None
        for name, value in profile_dict.items():
            setattr(self, name, self._wrap(value))

    def _wrap(self, value):
        if isinstance(value, (tuple, list, set, frozenset)): 
            return type(value)([self._wrap(v) for v in value])
        else:
            return Profile(value) if isinstance(value, dict) else value

class Result():
    def __init__(self):
        self.subtotal = None
        self.shipping = None
        self.tax = None
        self.total = None

class Bot():
    def __init__(self, shopping_cart_url):
        self.shopping_cart_url = shopping_cart_url

    def start(self):
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless") # https://stackoverflow.com/a/70125885/14775744
        self.driver = webdriver.Firefox(options=options)
        self.driver.set_window_size(1280, 949)

    def stop(self):
        self.driver.stop_client() # This needs to be added in order to close the window
        self.driver.quit()

    def run(self, product_url: str, p: Profile):
        raise Exception("run method not implemented for class {}".format(self.__class__.__name__))
        