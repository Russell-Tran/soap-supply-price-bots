import pytest
import json
from context import bot, sites
from helper import *
from sites import *

@pytest.mark.parametrize(('profile_json', 'product_url'),[
                         ('tests/example_profile.json', "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil"),
                         ('tests/example_profile.json', "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/cavalier-fragrance-oil"),
                         ('tests/example_profile_penn.json', "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil"),
                         ('tests/example_profile_penn.json', "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/cavalier-fragrance-oil")])
def test_nurture_soap(profile_json, product_url):
    result = generic_sim(NurtureSoap(), profile_json, product_url)
    assert exactly_one_price(result.subtotal)
    assert exactly_one_price(result.shipping)
    assert exactly_one_price(result.total)

def test_nurture_soap_advanced():
    result = generic_sim(NurtureSoap(), 'tests/example_profile.json', "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil")
    assert result.subtotal == "$4.00"
    assert result.shipping == "$7.92"
    assert result.total == "$11.92"