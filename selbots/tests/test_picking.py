from selbots.common import *
from selbots.sites import *
from selbots.picking import *

def test_picking():
    b = pick("https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil")
    assert b and isinstance(b, NurtureSoap)