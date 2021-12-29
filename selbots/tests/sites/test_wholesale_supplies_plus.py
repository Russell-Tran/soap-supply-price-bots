import pytest
import json
from tests.helper import *
from selbots.sites import *

@pytest.mark.parametrize(('profile_json', 'product_url'),[
                         ('tests/example_profile.json', "https://www.wholesalesuppliesplus.com/products/beeswax-white-ultra-refined-and-bleached.aspx"),
                         ('tests/example_profile_penn.json', "https://www.wholesalesuppliesplus.com/products/beeswax-white-ultra-refined-and-bleached.aspx")])
def test_nurture_soap(profile_json, product_url):
    result = generic_sim(WholesaleSuppliesPlus(), profile_json, product_url)
    assert exactly_one_price(result.subtotal)
    assert exactly_one_price(result.shipping)
    assert exactly_one_price(result.total)
