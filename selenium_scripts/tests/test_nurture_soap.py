import json
from context import bot, sites, exactly_one_price
from bot import *
from sites import *

def test_nurture_soap():
    with open('tests/example_profile.json') as file:
        profile = Profile(json.load(file))
        product_url = "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil"
        shopping_cart_url = "https://nurturesoap.com/cart"
        b = NurtureSoap()
        b.start()
        try:
            result = b.run(product_url, shopping_cart_url, profile)
        except Exception as e:
            b.stop()
            raise e
        b.stop()
        assert exactly_one_price(result.subtotal)
        assert exactly_one_price(result.shipping)
        assert exactly_one_price(result.total)

def test_nurture_soap_advanced():
    with open('tests/example_profile.json') as file:
        profile = Profile(json.load(file))
        product_url = "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil"
        shopping_cart_url = "https://nurturesoap.com/cart"
        b = NurtureSoap()
        b.start()
        try:
            result = b.run(product_url, shopping_cart_url, profile)
        except Exception as e:
            b.stop()
            raise e
        b.stop()
        assert result.subtotal == "$4.00"
        assert result.shipping == "$7.92"
        assert result.total == "$11.92"