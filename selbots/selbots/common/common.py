"""
Zap Sourcing 2021
"""
# Used here
from abc import ABC, abstractmethod
from ast import excepthandler
# Used here and children
from typing import List
import pint.quantity
import quantulum3.parser
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
from selenium.webdriver.remote.webelement import WebElement

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
        if (unit != 'dollar' 
            and unit != 'dimensionless' 
            and unit != 'percentage'):
            return q
    return None

"""
Other heuristic to convert some of the unit names
"""
def _extract_quantity_helper_rename(unit: str) -> str:
    if unit == 'pound-mass':
        return 'pound'
    if unit == 'pound sterling':
        return 'pound'
    if unit == 'fluid ounce':
        return 'floz'
    return unit

"""
Captures quantity from unstructured text rather intelligently
Returns quantity in pint Quantity in base units, None if not found

(Internally uses the quantulum3 Quantity class and then converts it to pint Quantity class)
"""
def extract_quantity(text: str) -> pint.quantity.Quantity:
    q = extract_quantity_nonbase(text)
    return q.to_base_units() if q else None

"""
Must convert to base units if you want to do manipulations reliably (see extract_quantity above)
"""
def extract_quantity_nonbase(text: str) -> pint.quantity.Quantity:
    # Quantulum can parse
    quant_intermediates = quantulum3.parser.parse(text)
    if len(quant_intermediates) == 0:
        return None
    quant_intermediate = _extract_quantity_helper_filter(quant_intermediates)
    if not quant_intermediate:
        return None

    # Pint can make the quantity manipulatable 
    value = quant_intermediate.value
    unit_name = _extract_quantity_helper_rename(quant_intermediate.unit.name)
    quant_final = GLOBAL_UREG.Quantity(value, unit_name)
    return quant_final


 # ==========================================================

def ugly_interventionist_ureg():
    # NOTE: This is a quick hack inspired from https://stackoverflow.com/questions/50866545/volume-to-mass-transformation-not-recognized-in-pint
    # Have not thought about this deeply
    # Main reason is to be able to interchange between mass and volume
    ureg = pint.UnitRegistry()
    c = pint.Context('ctx')
    def vtom(ureg, x):
        print ("vtom(%s, %s)" % (ureg, x))
        density = 1.0 * ureg.gram / ureg.ml
        return x/density
    def vtom2(ureg, x):
        print ("vtom2(%s, %s)" % (ureg, x))
        density = 1.0 * ureg.gram / ureg.ml
        return x*density
    c.add_transformation('[volume]', '[mass]', vtom2)
    c.add_transformation('[mass]', '[volume]', vtom)
    ureg.add_context(c)
    return ureg

# Really bad form but oh well 
GLOBAL_UREG = ugly_interventionist_ureg()

"""
Given a list of Quantities and a target Quantity,
returns the index of the element with the shortest distance

(Ok if list contains some None elements)
"""
def shortest_dist_idx(choices: List[pint.quantity.Quantity], target: pint.quantity.Quantity) -> int:
    try:
        _, idx = min([(abs(target - q), i) for i, q in enumerate(choices) if q is not None])
    except pint.errors.DimensionalityError:
        # TODO: UNIT TEST THIS AND ALSO MAKE IT MORE ROBUST / LOGICAL
        # TODO: Do vice versa for target as well (make all the things adhere to the target)
        # We had a stupid edge case where a menu used all of floz, oz, and lb
        # And so have to patch this dimensionality disagreement between volume and weight
        # https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil?variant=21140006895693
        # TODO: One way to implement this would be to convert floz to oz based on weight of water, and some
        # similar batching for all things like this. For now we are just going to ignore the choice of floz
        """
        # This is silly but basically for now we are repeating the code above except skipping any option that causes an error
        refined_choices = []
        for i, q in enumerate(choices):
            try:
                difference = abs(target - q)
                refined_choices.append((difference, i))
            except:
                continue
        _, idx = min(refined_choices)
        """

        # NOTE: This is a quick hack inspired from https://stackoverflow.com/questions/50866545/volume-to-mass-transformation-not-recognized-in-pint
        # Have not thought about this deeply
        try:
            choices =  [q.to('floz', 'ctx') for q in choices]
            _, idx = min([(abs(target - q), i) for i, q in enumerate(choices) if q is not None])
        except:
            try: 
                choices =  [q.to('gram', 'ctx') for q in choices]
                _, idx = min([(abs(target - q), i) for i, q in enumerate(choices) if q is not None])
            except Exception as e:
                raise e
                # This is so ugly i am very sorry

    return idx




 # ==========================================================

class Menu():
    """ 
    `candidate_elements` is a list of webelements which represent potential outcomes to a choice
    `qty_texts` is a list of unstructured texts which each correspond to the candidate_elements by index

    `candidate_elements` and `qty_texts` must be the same length
    """
    def __init__(self, candidate_elements: List[WebElement], qty_texts: List[str]):
        if len(candidate_elements) != len(qty_texts):
            raise Exception("length of parameter candidate_elements did not match length of parameter qty_texts")
        self.candidate_elements = candidate_elements
        self.quantities_pretty = [extract_quantity_nonbase(qty_text) for qty_text in qty_texts] # FOR COSMETIC ONLY, NOT CALC
        self.quantities = [q.to_base_units() if q else None for q in self.quantities_pretty] # USABLE FOR CALC
       
    def choose_element(self, target: pint.quantity.Quantity) -> (WebElement, pint.quantity.Quantity):
        idx = shortest_dist_idx(self.quantities, target)
        return (self.candidate_elements[idx], self.quantities_pretty[idx])

    def first_viable_element(self) -> (WebElement, pint.quantity.Quantity):
        for element, qty in zip(self.candidate_elements, self.quantities_pretty):
            if qty is not None:
                return (element, qty)

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
        self.size: pint.quantity.Quantity = None

class Bot(ABC):
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

    @abstractmethod
    def run(self, product_url: str, p: Profile, target_qty: pint.quantity.Quantity):
        raise Exception("run method not implemented for class {}".format(self.__class__.__name__))

    """ Assumes you've already got the page open and everything. (Assumes you're inside the run method).
    Just some space to write logic to scrape the menu and ingest in as a Menu object.
    """
    def _generate_menu(self) -> Menu:
        raise Exception("generate_menu method not implemented for class {}".format(self.__class__.__name__))
        