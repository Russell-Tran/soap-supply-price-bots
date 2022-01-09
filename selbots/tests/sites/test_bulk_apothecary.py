import pytest
import json
from tests.helper import *
from selbots.sites import *

basic_url = "https://www.bulkapothecary.com/product/raw-ingredients/waxes-and-butters/beeswax-white-and-yellow/"

@pytest.mark.parametrize(('profile_json', 'product_url'),[
                         ('tests/example_profile.json', basic_url),
                         ('tests/example_profile_penn.json', basic_url)])
def test_bulk_apothecary(profile_json, product_url):
    result = generic_sim(BulkApothecary(), profile_json, product_url)
    exactly_one_price_assertions(result)

def test_bulk_apothecary_qty_1():
    url = "https://www.bulkapothecary.com/product/raw-ingredients/waxes-and-butters/beeswax-white-and-yellow/"
    result = generic_sim_qty(BulkApothecary(), 'tests/example_profile_penn.json', url, "1 lbs")
    assert "1.0 pound" in str(result.size)

def test_bulk_apothecary_qty_2():
    url = "https://www.bulkapothecary.com/product/raw-ingredients/waxes-and-butters/beeswax-white-and-yellow/"
    result = generic_sim_qty(BulkApothecary(), 'tests/example_profile_penn.json', url, "55 lbs")
    assert "55.0 pound" in str(result.size)

def test_bulk_apothecary_qty_3():
    url = "https://www.bulkapothecary.com/product/raw-ingredients/waxes-and-butters/beeswax-white-and-yellow/"
    result = generic_sim_qty(BulkApothecary(), 'tests/example_profile_penn.json', url, "5 lbs")
    assert "4.0 pound" in str(result.size)

def test_bulk_apothecary_qty_4():
    url = "https://www.bulkapothecary.com/product/raw-ingredients/waxes-and-butters/beeswax-white-and-yellow/"
    result = generic_sim_qty(BulkApothecary(), 'tests/example_profile_penn.json', url, "4 lbs")
    assert "4.0 pound" in str(result.size)