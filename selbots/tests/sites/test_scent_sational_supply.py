import pytest
import json
from tests.helper import *
from selbots.sites import *

basic_url = "https://scentsationalsupply.com/peak-candle-type/watermelon-peak-type"

@pytest.mark.parametrize(('profile_json', 'product_url'),[
                         ('tests/example_profile.json', basic_url),
                         ('tests/example_profile_penn.json', basic_url)])
def test_scent_sational_supply(profile_json, product_url):
    result = generic_sim(ScentSationalSupply(), profile_json, product_url)
    exactly_one_price_assertions(result)

def test_scent_sational_supply_qty_1():
    url = "https://scentsationalsupply.com/peak-candle-type/watermelon-peak-type"
    result = generic_sim_qty(ScentSationalSupply(), 'tests/example_profile_penn.json', url, "1 floz")
    assert "4.0 fluid_ounce" in str(result.size)

def test_scent_sational_supply_qty_2():
    url = "https://scentsationalsupply.com/peak-candle-type/watermelon-peak-type"
    result = generic_sim_qty(ScentSationalSupply(), 'tests/example_profile_penn.json', url, "4 floz")
    assert "4.0 fluid_ounce" in str(result.size)

def test_scent_sational_supply_qty_3():
    url = "https://scentsationalsupply.com/peak-candle-type/watermelon-peak-type"
    result = generic_sim_qty(ScentSationalSupply(), 'tests/example_profile_penn.json', url, "8 floz")
    assert "8.0 fluid_ounce" in str(result.size)

def test_scent_sational_supply_qty_4():
    url = "https://scentsationalsupply.com/peak-candle-type/watermelon-peak-type"
    result = generic_sim_qty(ScentSationalSupply(), 'tests/example_profile_penn.json', url, "16 floz")
    assert "16.0 fluid_ounce" in str(result.size)

