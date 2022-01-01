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
