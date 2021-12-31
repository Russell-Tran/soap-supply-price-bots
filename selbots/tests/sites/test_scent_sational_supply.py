import pytest
import json
from tests.helper import *
from selbots.sites import *

basic_url = "https://scentsationalsupply.com/additives-for-soapmaking/water-soluble-titanium-dioxide"

@pytest.mark.parametrize(('profile_json', 'product_url'),[
                         ('tests/example_profile.json', "https://scentsationalsupply.com/additives-for-soapmaking/water-soluble-titanium-dioxide"),
                         ('tests/example_profile_penn.json', "https://scentsationalsupply.com/additives-for-soapmaking/water-soluble-titanium-dioxide")])
def test_nurture_soap(profile_json, product_url):
    result = generic_sim(ScentSationalSupply(), profile_json, product_url)
    exactly_one_price_assertions(result)
