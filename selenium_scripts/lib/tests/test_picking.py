from context import bot, picking
from bot import *
from sites import *

def test_picking():
    b = picking.pick("https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil")
    assert b and isinstance(b, NurtureSoap)