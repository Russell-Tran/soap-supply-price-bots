import pytest
import json
from tests.helper import *
from selbots.sites import *

basic_url = "https://mountainroseherbs.com/beeswax"

@pytest.mark.parametrize(('profile_json', 'product_url'),[
                         ('tests/example_profile.json', basic_url),
                         ('tests/example_profile_penn.json', basic_url)])
def test_mountain_rose_herbs(profile_json, product_url):
    result = generic_sim(MountainRoseHerbs(), profile_json, product_url)
    exactly_one_price_assertions(result)

def test_mountain_rose_herbs_qty_1():
    url = "https://mountainroseherbs.com/beeswax"
    result = generic_sim_qty(MountainRoseHerbs(), 'tests/example_profile_penn.json', url, "1 oz")
    assert "1.0 ounce" in str(result.size)

def test_mountain_rose_herbs_qty_2():
    url = "https://mountainroseherbs.com/beeswax"
    result = generic_sim_qty(MountainRoseHerbs(), 'tests/example_profile_penn.json', url, "1 lb")
    assert "1.0 pound" in str(result.size)

def test_mountain_rose_herbs_qty_3():
    url = "https://mountainroseherbs.com/beeswax"
    result = generic_sim_qty(MountainRoseHerbs(), 'tests/example_profile_penn.json', url, "5 lb")
    assert "5.0 pound" in str(result.size)

def test_mountain_rose_herbs_qty_4():
    url = "https://mountainroseherbs.com/beeswax"
    result = generic_sim_qty(MountainRoseHerbs(), 'tests/example_profile_penn.json', url, "16 oz")
    assert "1.0 pound" in str(result.size)