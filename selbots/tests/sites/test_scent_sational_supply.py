import pytest
import json
from tests.helper import *
from selbots.sites import *

@pytest.mark.parametrize(('profile_json', 'product_url'),[
                         ('tests/example_profile.json', "https://scentsationalsupply.com/additives-for-soapmaking/water-soluble-titanium-dioxide"),
                         ('tests/example_profile_penn.json', "https://scentsationalsupply.com/additives-for-soapmaking/water-soluble-titanium-dioxide")])
def test_nurture_soap(profile_json, product_url):
    result = generic_sim(ScentSationalSupply(), profile_json, product_url)
    assert exactly_one_price(result.subtotal)
    assert exactly_one_price(result.shipping)
    assert exactly_one_price(result.total)
