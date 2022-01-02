import json
import pint
from selbots.common import *

def test_profile():
    with open('tests/example_profile.json') as file:
        profile = Profile(json.load(file))
        assert profile.first_name == "John"
        assert profile.last_name == "Snow"
        assert profile.email == "winteriscoming@gmail.com"
        assert profile.phone == "(949) 361-8200"
        assert profile.fax == "(949) 493-8729"
        assert profile.company == "Cool Soap, Inc."
        assert profile.address == "15 Calle Loyola"
        assert profile.address_2 == "Suite #15"
        assert profile.city == "San Clemente"
        assert profile.state == "California"
        assert profile.country == "United States"
        assert profile.zipcode == "92673"

def test_extract_quantity():
    ureg = pint.UnitRegistry()
    assert extract_quantity("I want 2 liters of wine") == (2 * ureg.liter).to_base_units() 
    assert extract_quantity("$52.71 for 1 Block (10 lb)") == (10 * ureg.lb).to_base_units()
    assert extract_quantity("$6.38 for 2 oz") == (2 * ureg.oz).to_base_units()
    assert extract_quantity("1oz Jar    ($2.75) Out of Stock  ") == (1 * ureg.oz).to_base_units()
    assert extract_quantity("1 pound bag    ($32.75)   ") == (1 * ureg.lb).to_base_units()
    assert extract_quantity("$10.28 for 1 lb") == (1 * ureg.lb).to_base_units()
    assert extract_quantity("1 fl. oz") == (10 * ureg.floz).to_base_units()
    assert extract_quantity("1 lb") == (1 * ureg.lb).to_base_units()
    assert extract_quantity("Bees Wax Pastilles Pearls - Yellow - 8 lbs") == (8 * ureg.lb).to_base_units()
    assert extract_quantity("1 oz.") == (1 * ureg.oz).to_base_units()
    assert extract_quantity("5 lb.") == (5 * ureg.lb).to_base_units()
    assert extract_quantity("Natural Yellow Beeswax 2lbs ($9.05 /lb)   (") == (2 * ureg.lb).to_base_units()
    assert extract_quantity("Beeswax - Yellow Granules - (Origin: USA) - 5 kg (11 lbs)") == (5 * ureg.kg).to_base_units()
    assert extract_quantity("55 lb White ($4.74 / lb) - $260.59***") == (55 * ureg.lb).to_base_units()
    assert extract_quantity("1 lb Yellow - $9.36") == (1 * ureg.lb).to_base_units()
    assert extract_quantity(r"Orders over $250 take an additional 15% off using coupon code 15off250") == None
    
    
    #print(2.0 * ureg.liter )