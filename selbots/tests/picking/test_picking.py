import pytest
from selbots.common import *
from selbots.sites import *
from selbots.picking import *

@pytest.mark.parametrize(('class_type', 'product_url'),[
    (NurtureSoap, "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil"),
    (ScentSationalSupply, "https://scentsationalsupply.com/additives-for-soapmaking/water-soluble-titanium-dioxide"),
])
def test_picking(class_type, product_url):
    b = pick(product_url)
    assert b and isinstance(b, class_type)
