import pytest
import json
from tests.helper import *
from selbots.sites import *

basic_url = "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil"

@pytest.mark.parametrize(('profile_json', 'product_url'),[
                         ('tests/example_profile.json', "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil"),
                         ('tests/example_profile.json', "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/cavalier-fragrance-oil"),
                         ('tests/example_profile_penn.json', "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil"),
                         ('tests/example_profile_penn.json', "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/cavalier-fragrance-oil")])
def test_nurture_soap(profile_json, product_url):
    result = generic_sim(NurtureSoap(), profile_json, product_url)
    exactly_one_price_assertions(result)

def test_nurture_soap_advanced():
    result = generic_sim(NurtureSoap(), 'tests/example_profile.json', "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil")
    assert result.subtotal == "$4.00"
    assert result.shipping == "$7.59"
    assert result.total == "$11.86"