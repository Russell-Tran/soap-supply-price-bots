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
    assert extract_quantity("1 fl. oz") == (1 * ureg.floz).to_base_units()
    assert extract_quantity("1 lb") == (1 * ureg.lb).to_base_units()
    assert extract_quantity("Bees Wax Pastilles Pearls - Yellow - 8 lbs") == (8 * ureg.lb).to_base_units()
    assert extract_quantity("1 oz.") == (1 * ureg.oz).to_base_units()
    assert extract_quantity("5 lb.") == (5 * ureg.lb).to_base_units()
    assert extract_quantity("Natural Yellow Beeswax 2lbs ($9.05 /lb)   (") == (2 * ureg.lb).to_base_units()
    assert extract_quantity("Beeswax - Yellow Granules - (Origin: USA) - 5 kg (11 lbs)") == (5 * ureg.kg).to_base_units()
    assert extract_quantity("55 lb White ($4.74 / lb) - $260.59***") == (55 * ureg.lb).to_base_units()
    assert extract_quantity("1 lb Yellow - $9.36") == (1 * ureg.lb).to_base_units()
    assert extract_quantity(r"Orders over $250 take an additional 15% off using coupon code 15off250") == None
    
def test_shortest_dist_idx():
    target = pint.quantity.Quantity(5.0, "oz")
    choices = [
        pint.quantity.Quantity(8.0, "oz"),
        pint.quantity.Quantity(3.0, "oz"),
        pint.quantity.Quantity(2.0, "oz"),
        pint.quantity.Quantity(10.0, "oz"),
        pint.quantity.Quantity(25.0, "oz"),
        pint.quantity.Quantity(550.0, "oz")
    ]
    assert shortest_dist_idx(choices, target) == 1

    target = pint.quantity.Quantity(8.5, "oz")
    choices = [
        pint.quantity.Quantity(8.0, "oz"),
        pint.quantity.Quantity(3.0, "oz"),
        pint.quantity.Quantity(2.0, "oz"),
        pint.quantity.Quantity(10.0, "oz"),
        pint.quantity.Quantity(25.0, "oz"),
        pint.quantity.Quantity(550.0, "oz")
    ]
    assert shortest_dist_idx(choices, target) == 0

    target = pint.quantity.Quantity(60000, "oz")
    choices = [
        pint.quantity.Quantity(8.0, "oz"),
        pint.quantity.Quantity(3.0, "oz"),
        pint.quantity.Quantity(2.0, "oz"),
        pint.quantity.Quantity(10.0, "oz"),
        pint.quantity.Quantity(25.0, "oz"),
        pint.quantity.Quantity(550.0, "oz")
    ]
    assert shortest_dist_idx(choices, target) == 5

def test_shortest_dist_idx_different_unit():
    target = pint.quantity.Quantity(1, "lb")
    choices = [
        pint.quantity.Quantity(8.0, "oz"),
        pint.quantity.Quantity(3.0, "oz"),
        pint.quantity.Quantity(2.0, "oz"),
        pint.quantity.Quantity(10.0, "oz"),
        pint.quantity.Quantity(25.0, "oz"),
        pint.quantity.Quantity(550.0, "oz"),
        pint.quantity.Quantity(16.2, "oz"),
        pint.quantity.Quantity(10.0, "oz")
    ]
    assert shortest_dist_idx(choices, target) == 6

    target = pint.quantity.Quantity(141.748, "g")
    choices = [
        pint.quantity.Quantity(8.0, "oz"),
        pint.quantity.Quantity(3.0, "oz"),
        pint.quantity.Quantity(2.0, "oz"),
         pint.quantity.Quantity(5.0, "oz"),
        pint.quantity.Quantity(10.0, "oz"),
        pint.quantity.Quantity(25.0, "oz"),
        pint.quantity.Quantity(550.0, "oz"),
        pint.quantity.Quantity(16.2, "oz"),
        pint.quantity.Quantity(10.0, "oz")
    ]
    assert shortest_dist_idx(choices, target) == 3

    target = pint.quantity.Quantity(10, "floz")
    choices = [
        pint.quantity.Quantity(100, "mL"),
        pint.quantity.Quantity(200, "mL"),
        pint.quantity.Quantity(300, "mL"),
        pint.quantity.Quantity(400, "mL"),
    ]
    assert shortest_dist_idx(choices, target) == 2

    target = pint.quantity.Quantity(10, "floz")
    choices = [
        pint.quantity.Quantity(100, "L"),
        pint.quantity.Quantity(200, "L"),
        pint.quantity.Quantity(300, "L"),
        pint.quantity.Quantity(400, "L"),
    ]
    assert shortest_dist_idx(choices, target) == 0

def test_shortest_dist_idx_has_none():
    target = pint.quantity.Quantity(5.0, "oz")
    choices = [
        pint.quantity.Quantity(8.0, "oz"),
        pint.quantity.Quantity(3.0, "oz"),
        pint.quantity.Quantity(2.0, "oz"),
        pint.quantity.Quantity(10.0, "oz"),
        None,
        pint.quantity.Quantity(550.0, "oz")
    ]
    assert shortest_dist_idx(choices, target) == 1

    target = pint.quantity.Quantity(8.5, "oz")
    choices = [
        pint.quantity.Quantity(8.0, "oz"),
        pint.quantity.Quantity(3.0, "oz"),
        pint.quantity.Quantity(2.0, "oz"),
        pint.quantity.Quantity(10.0, "oz"),
        pint.quantity.Quantity(25.0, "oz"),
        None,
        None,
        pint.quantity.Quantity(550.0, "oz"),
        None
    ]
    assert shortest_dist_idx(choices, target) == 0

def test_menu():
    c = [
        WebElement("junk", "alpha"),
        WebElement("junk", "beta"),
        WebElement("junk", "gamma"),
        WebElement("junk", "delta"),
        WebElement("junk", "epsilon"),
    ]
    qty_texts = ['', '1 lb', '5 lbs', '25 lbs', '55 lbs']
    m = Menu(c, qty_texts)
    assert m.choose_element(pint.quantity.Quantity(1.0, "lb"))[0] == c[1]
    assert m.choose_element(pint.quantity.Quantity(5.0, "lb"))[0] == c[2]
    assert m.choose_element(pint.quantity.Quantity(25.0, "lb"))[0] == c[3]
    assert m.choose_element(pint.quantity.Quantity(55.0, "lb"))[0] == c[4]
    assert m.choose_element(pint.quantity.Quantity(16, "oz"))[0] == c[1]
    assert m.choose_element(pint.quantity.Quantity(100, "lb"))[0] == c[4]

    assert m.choose_element(pint.quantity.Quantity(1.5, "lb"))[0] == c[1]
    assert m.choose_element(pint.quantity.Quantity(5.5, "lb"))[0] == c[2]
    assert m.choose_element(pint.quantity.Quantity(25.5, "lb"))[0] == c[3]
    assert m.choose_element(pint.quantity.Quantity(55.5, "lb"))[0] == c[4]
    assert m.choose_element(pint.quantity.Quantity(16.5, "oz"))[0] == c[1]
    assert m.choose_element(pint.quantity.Quantity(100.5, "lb"))[0] == c[4]

    assert m.choose_element(pint.quantity.Quantity(0.5, "lb"))[0] == c[1]
    assert m.choose_element(pint.quantity.Quantity(4.5, "lb"))[0] == c[2]
    assert m.choose_element(pint.quantity.Quantity(24.5, "lb"))[0] == c[3]
    assert m.choose_element(pint.quantity.Quantity(54.5, "lb"))[0] == c[4]
    assert m.choose_element(pint.quantity.Quantity(15.5, "oz"))[0] == c[1]
    assert m.choose_element(pint.quantity.Quantity(99.5, "lb"))[0] == c[4]
    