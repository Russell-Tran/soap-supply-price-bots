import pytest
import json
from tests.helper import *
from selbots.sites import *

basic_url = "https://www.chemistrystore.com/Cosmetic_Waxes-Natural_Yellow_Beeswax.html"

@pytest.mark.parametrize(('profile_json', 'product_url'),[
                         ('tests/example_profile.json', basic_url),
                         ('tests/example_profile_penn.json', basic_url)])
def test_chemistry_store(profile_json, product_url):
    result = generic_sim(ChemistryStore(), profile_json, product_url)
    exactly_one_price_assertions(result)
