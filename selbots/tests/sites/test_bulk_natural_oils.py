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
