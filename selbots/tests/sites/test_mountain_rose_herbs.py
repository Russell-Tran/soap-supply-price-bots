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
