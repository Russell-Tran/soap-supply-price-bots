import pytest
import json
from tests.helper import *
from selbots.sites import *

basic_url = "https://www.wholesalesuppliesplus.com/products/beeswax-white-ultra-refined-and-bleached.aspx"
basic_profile = 'tests/example_profile.json'

@pytest.mark.parametrize(('profile_json', 'product_url'),[
                         ('tests/example_profile.json', basic_url),
                         ('tests/example_profile_penn.json', basic_url)])
def test_wholesale_supplies_plus(profile_json, product_url):
    result = generic_sim(WholesaleSuppliesPlus(), profile_json, product_url)
    exactly_one_price_assertions(result)
