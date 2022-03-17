"""
Use this script for manual inspection of scripts
"""

from tests.helper import *
from tests.sites.test_wholesale_supplies_plus import basic_url
#from tests.sites.test_scent_sational_supply import basic_url
# from tests.sites.test_nurture_soap import basic_url
#from tests.sites.test_brambleberry import basic_url
#from tests.sites.test_bulk_natural_oils import basic_url
#from tests.sites.test_bulk_apothecary import basic_url
#from tests.sites.test_mountain_rose_herbs import basic_url
#from tests.sites.test_essential_depot import basic_url
#from tests.sites.test_chemistry_store import basic_url
from selbots.sites import *
basic_profile = 'tests/example_profile.json'
basic_penn_profile = 'tests/example_profile_penn.json'


import pint.quantity
from quantulum3 import parser as quantparser


if __name__ == "__main__":



    print_result(generic_sim_qty(EssentialDepot(headless=False), basic_profile, "https://www.essentialdepot.com/product/COCONUT-1-QUART.html", '5 lbs'))


    # result = generic_sim(BulkNaturalOils(headless=False), basic_penn_profile, basic_url)
    # print_result(result)

    # quant_intermediate = quantparser.parse('I want 2 liters of wine')[0]
    # quant = pint.quantity.Quantity(float(str(quant_intermediate.value)), str(quant_intermediate.unit)) # must cast val to float (https://github.com/hgrecco/pint/issues/538)
    # print(quant)

    #ureg = pint.UnitRegistry()
    #print(extract_quantity("$52.71 for 1 Block (10 lb)"))
    #print((10 * ureg.lb).to_base_units())
    #extract_quantity("1 pound bag    ($32.75)   ") == (1 * ureg.lb).to_base_units()
    #print(extract_quantity("$10.28 for 1 lb") == (1 * ureg.lb).to_base_units())
    #extract_quantity("1 fl. oz") == (10 * ureg.floz).to_base_units()

    #print_result(generic_sim_qty(WholesaleSuppliesPlus(headless=False), basic_profile, basic_url, '5 lbs'))

    #bno_url = "https://bulknaturaloils.com/coconut-oil-rbd.html"
    #print_result(generic_sim_qty(BulkNaturalOils(headless=False), basic_profile, bno_url , '5 lbs'))

    #basic_url = "https://scentsationalsupply.com/peak-candle-type/watermelon-peak-type"
    #print_result(generic_sim_qty(ScentSationalSupply(headless=False), basic_profile, basic_url, '8 floz'))
