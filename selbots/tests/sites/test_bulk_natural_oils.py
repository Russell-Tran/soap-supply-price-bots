import pytest
import json
from tests.helper import *
from selbots.sites import *

basic_url = "https://bulknaturaloils.com/beeswax-yellow-granules.html"

@pytest.mark.parametrize(('profile_json', 'product_url'),[
                         ('tests/example_profile.json', basic_url),
                         ('tests/example_profile_penn.json', basic_url)])
def test_bulk_natural_oils(profile_json, product_url):
    result = generic_sim(BulkNaturalOils(), profile_json, product_url)
    exactly_one_price_assertions(result)

def test_bulk_natural_oils_qty_1():
    url = "https://bulknaturaloils.com/beeswax-yellow-granules.html"
    result = generic_sim_qty(BulkNaturalOils(), 'tests/example_profile_penn.json', url, "12.5 kg")
    assert "12.5 kilogram" in str(result.size)

def test_bulk_natural_oils_qty_2():
    url = "https://bulknaturaloils.com/beeswax-yellow-granules.html"
    result = generic_sim_qty(BulkNaturalOils(), 'tests/example_profile_penn.json', url, "11 lbs")
    assert "5.0 kilogram" in str(result.size)