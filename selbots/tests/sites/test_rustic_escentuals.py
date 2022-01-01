import pytest
import json
from tests.helper import *
from selbots.sites import *

basic_url = "https://www.rusticescentuals.com/products/White-Beeswax-Pastilles-16-ounces.aspx"

@pytest.mark.parametrize(('profile_json', 'product_url'),[
                         ('tests/example_profile.json', basic_url),
                         ('tests/example_profile_penn.json', basic_url)])
def test_rustic_escentuals(profile_json, product_url):
    result = generic_sim(RusticEscentuals(), profile_json, product_url)
    exactly_one_price_assertions(result)
