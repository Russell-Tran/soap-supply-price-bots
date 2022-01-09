import pytest
import json
from tests.helper import *
from selbots.sites import *

basic_url = "https://www.brambleberry.com/shop-by-product/ingredients/waxes/premium-yellow-beeswax/V001192.html"

@pytest.mark.parametrize(('profile_json', 'product_url'),[
                         ('tests/example_profile.json', basic_url),
                         ('tests/example_profile_penn.json', basic_url)])
def test_brambleberry(profile_json, product_url):
    result = generic_sim(Brambleberry(), profile_json, product_url)
    exactly_one_price_assertions(result)

def test_brambleberry_qty_1():
    url = "https://www.brambleberry.com/shop-by-product/ingredients/waxes/premium-yellow-beeswax/V001192.html"
    result = generic_sim_qty(Brambleberry(), 'tests/example_profile_penn.json', url, "5 lbs")
    assert "5.0 pound" in str(result.size)

def test_brambleberry_qty_2():
    url = "https://www.brambleberry.com/shop-by-product/ingredients/waxes/premium-yellow-beeswax/V001192.html"
    result = generic_sim_qty(Brambleberry(), 'tests/example_profile_penn.json', url, "55 lbs")
    assert "55.0 pound" in str(result.size)

def test_brambleberry_qty_3():
    url = "https://www.brambleberry.com/shop-by-product/ingredients/waxes/premium-yellow-beeswax/V001192.html"
    result = generic_sim_qty(Brambleberry(), 'tests/example_profile_penn.json', url, "60 lbs")
    assert "55.0 pound" in str(result.size)