import pytest
import json
from tests.helper import *
from selbots.sites import *

basic_url = "https://www.wholesalesuppliesplus.com/products/beeswax-white-ultra-refined-and-bleached.aspx"

@pytest.mark.parametrize(('profile_json', 'product_url'),[
                         ('tests/example_profile.json', basic_url),
                         ('tests/example_profile_penn.json', basic_url)])
def test_wholesale_supplies_plus(profile_json, product_url):
    result = generic_sim(WholesaleSuppliesPlus(), profile_json, product_url)
    exactly_one_price_assertions(result)

def test_wholesale_supplies_plus_qty_1():
    url = "https://www.wholesalesuppliesplus.com/products/beeswax-white-ultra-refined-and-bleached.aspx"
    result = generic_sim_qty(WholesaleSuppliesPlus(), 'tests/example_profile_penn.json', url, "2 oz")
    assert "2.0 ounce" in str(result.size)

def test_wholesale_supplies_plus_qty_2():
    url = "https://www.wholesalesuppliesplus.com/products/beeswax-white-ultra-refined-and-bleached.aspx"
    result = generic_sim_qty(WholesaleSuppliesPlus(), 'tests/example_profile_penn.json', url, "1 lb")
    assert "1.0 pound" in str(result.size)

def test_wholesale_supplies_plus_qty_3():
    url = "https://www.wholesalesuppliesplus.com/products/beeswax-white-ultra-refined-and-bleached.aspx"
    result = generic_sim_qty(WholesaleSuppliesPlus(), 'tests/example_profile_penn.json', url, "5 lbs")
    assert "5.0 pound" in str(result.size)

def test_wholesale_supplies_plus_qty_4():
    url = "https://www.wholesalesuppliesplus.com/products/beeswax-white-ultra-refined-and-bleached.aspx"
    result = generic_sim_qty(WholesaleSuppliesPlus(), 'tests/example_profile_penn.json', url, "55 lbs")
    assert "55.0 pound" in str(result.size)

def test_wholesale_supplies_plus_qty_5():
    url = "https://www.wholesalesuppliesplus.com/products/beeswax-white-ultra-refined-and-bleached.aspx"
    result = generic_sim_qty(WholesaleSuppliesPlus(), 'tests/example_profile_penn.json', url, "550 lbs")
    assert "550.0 pound" in str(result.size)