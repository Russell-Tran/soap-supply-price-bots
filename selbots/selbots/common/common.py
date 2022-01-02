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

# Used here and children
from typing import List
import pint.quantity
import quantulum3.parser

# Constant used when a particular website doesn't have a Result attribute (e.g. no fees)
FREE_PRICE = "$0.00"

"""
Used for `selenium.common.exceptions.MoveTargetOutOfBoundsException: 
Message: (765, 957) is out of bounds of viewport width (1280) and height (864)`

Source: https://stackoverflow.com/a/52045231/14775744
"""
def scroll_shim(passed_in_driver, object):
    x = object.location['x']
    y = object.location['y']
    scroll_by_coord = 'window.scrollTo(%s,%s);' % (
        x,
        y
    )
    scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
    passed_in_driver.execute_script(scroll_by_coord)
    passed_in_driver.execute_script(scroll_nav_out_of_way)
    return

"""
Heuristic that returns the first quantity whose unit isn't dollar or dimensionless (to filter those out)
"""
def _extract_quantity_helper_filter(quant_intermediates: List[quantulum3.classes.Quantity]) -> quantulum3.classes.Quantity:
    for q in quant_intermediates:
        unit = q.unit.name.lower()
        if unit != 'dollar' and unit != 'dimensionless':
            return q
    return None

"""
Other heuristic to convert the unit names
"""
def _extract_quantity_helper_rename(unit: str) -> str:
    if unit == 'pound-mass':
        return 'pound'
    if unit == 'pound sterling':
        return 'pound'
    return unit
# def _extract_quantity_helper_rename(quant_intermediate: quantulum3.classes.Quantity) -> quantulum3.classes.Quantity:
#     unit = quant_intermediate.unit.name.lower()
#     new_name = unit
#     if unit == 'pound-mass':
#         new_name = 'pound'
#     if unit == 'pound sterling':
#         new_name = 'pound'
#     quant_intermediate.unit.name = new_name
#     return quant_intermediate

"""
Captures quantity from unstructured text rather intelligently
Returns quantity in pint Quantity in base units

(Internally uses the quantulum3 Quantity class and then converts it to pint Quantity class)
"""
def extract_quantity(text: str) -> pint.quantity.Quantity:
    # Quantulum can parse
    quant_intermediates = quantulum3.parser.parse(text)
    if len(quant_intermediates) == 0:
        return None
    quant_intermediate = _extract_quantity_helper_filter(quant_intermediates)
    if not quant_intermediate:
        return None
    # Pint can make the quantity manipulatable 
    value = quant_intermediate.value
    unit = _extract_quantity_helper_rename(quant_intermediate.unit.name)
    quant_final = pint.quantity.Quantity(value, unit)
    return quant_final.to_base_units()

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
        self.fees = None
        self.tax = None
        self.total = None

class Bot():
    def __init__(self, shopping_cart_url, headless=True):
        self.shopping_cart_url = shopping_cart_url
        self.headless = headless

    def start(self):
        options = webdriver.FirefoxOptions()
        if self.headless:
            options.add_argument("--headless") # https://stackoverflow.com/a/70125885/14775744
        self.driver = webdriver.Firefox(options=options)
        self.driver.set_window_size(1280, 949)

    def stop(self):
        self.driver.stop_client() # This needs to be added in order to close the window
        self.driver.quit()

    def run(self, product_url: str, p: Profile):
        raise Exception("run method not implemented for class {}".format(self.__class__.__name__))


        