import pytest
import json
from tests.helper import *
from selbots.sites import *

basic_url = "https://www.essentialdepot.com/product/BEESWAX-YELLOW-8LBS.html"

@pytest.mark.parametrize(('profile_json', 'product_url'),[
                         ('tests/example_profile.json', basic_url),
                         ('tests/example_profile_penn.json', basic_url)])
def test_essential_depot(profile_json, product_url):
    result = generic_sim(EssentialDepot(), profile_json, product_url)
    exactly_one_price_assertions(result)

def test_essential_depot_qty_1():
    url = "https://www.essentialdepot.com/product/BEESWAX-YELLOW-8LBS.html"
    result = generic_sim_qty(EssentialDepot(), 'tests/example_profile_penn.json', url, "8 lbs")
    assert "8.0 pound" in str(result.size)

def test_essential_depot_qty_2():
    url = "https://www.essentialdepot.com/product/BEESWAX-YELLOW-8LBS.html"
    result = generic_sim_qty(EssentialDepot(), 'tests/example_profile_penn.json', url, "1000 lbs")
    assert "8.0 pound" in str(result.size)