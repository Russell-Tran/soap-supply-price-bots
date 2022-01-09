from tests.helper import *
#from tests.sites.test_wholesale_supplies_plus import basic_url
#from tests.sites.test_scent_sational_supply import basic_url
# from tests.sites.test_nurture_soap import basic_url
from tests.sites.test_brambleberry import basic_url
# from tests.sites.test_bulk_natural_oils import basic_url
#from tests.sites.test_bulk_apothecary import basic_url
#from tests.sites.test_mountain_rose_herbs import basic_url
#from tests.sites.test_essential_depot import basic_url
from selbots.sites import *
basic_profile = 'tests/example_profile.json'
basic_penn_profile = 'tests/example_profile_penn.json'


import pint.quantity
from quantulum3 import parser as quantparser


if __name__ == "__main__":
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

    generic_sim(Brambleberry(headless=False), basic_profile, basic_url)
