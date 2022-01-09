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

# def test_nurture_soap_advanced():
#     result = generic_sim(NurtureSoap(), 'tests/example_profile.json', "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil")
#     assert result.subtotal == "$4.00"
#     assert result.shipping == "$7.59"
#     assert result.total == "$11.86"

def test_nurture_soap_qty_1():
    url = "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil"
    result = generic_sim_qty(NurtureSoap(), 'tests/example_profile_penn.json', url, "1 floz")
    assert "1.0 fluid_ounce" in str(result.size)

def test_nurture_soap_qty_2():
    url = "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil"
    result = generic_sim_qty(NurtureSoap(), 'tests/example_profile_penn.json', url, "4 oz")
    assert "4.0 ounce" in str(result.size)

def test_nurture_soap_qty_3():
    url = "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil"
    result = generic_sim_qty(NurtureSoap(), 'tests/example_profile_penn.json', url, "8 oz")
    assert "8.0 ounce" in str(result.size)

def test_nurture_soap_qty_4():
    url = "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil"
    result = generic_sim_qty(NurtureSoap(), 'tests/example_profile_penn.json', url, "1 lb")
    assert "1.0 pound" in str(result.size)

def test_nurture_soap_qty_5():
    url = "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil"
    result = generic_sim_qty(NurtureSoap(), 'tests/example_profile_penn.json', url, "16 oz")
    assert "1.0 pound" in str(result.size)