from sheetsman import *
from sheetsman import __version__

def test_version():
    assert __version__ == '0.1.0'

def test_sanity():
    assert sanity("fantastic-engine-test")[0][0] == "howdy"