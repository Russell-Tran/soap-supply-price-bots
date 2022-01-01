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
