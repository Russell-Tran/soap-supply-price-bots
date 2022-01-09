import pytest
import json
from tests.helper import *
from selbots.sites import *

basic_url = "https://www.chemistrystore.com/Deodorant_Bottles-90ml_Rol-On_Deodorant_Bottles_1.html"

@pytest.mark.parametrize(('profile_json', 'product_url'),[
                         ('tests/example_profile.json', basic_url),
                         ('tests/example_profile_penn.json', basic_url)])
def test_chemistry_store(profile_json, product_url):
    result = generic_sim(ChemistryStore(), profile_json, product_url)
    exactly_one_price_assertions(result)

def test_chemistry_store_qty_1():
    url = "https://www.chemistrystore.com/Cosmetic_Waxes-Natural_Yellow_Beeswax.html"
    result = generic_sim_qty(ChemistryStore(), 'tests/example_profile_penn.json', url, "10 lbs")
    assert "10.0 pound" in str(result.size)

def test_chemistry_store_qty_2():
    url = "https://www.chemistrystore.com/Cosmetic_Waxes-Natural_Yellow_Beeswax.html"
    result = generic_sim_qty(ChemistryStore(), 'tests/example_profile_penn.json', url, "2 lbs")
    assert "2.0 pound" in str(result.size)

def test_chemistry_store_qty_2():
    url = "https://www.chemistrystore.com/Cosmetic_Waxes-Natural_Yellow_Beeswax.html"
    result = generic_sim_qty(ChemistryStore(), 'tests/example_profile_penn.json', url, "1 kg")
    assert "2.0 pound" in str(result.size)