from tests.helper import *
#from tests.sites.test_wholesale_supplies_plus import basic_url
#from tests.sites.test_scent_sational_supply import basic_url
# from tests.sites.test_nurture_soap import basic_url
#from tests.sites.test_brambleberry import basic_url
from tests.sites.test_bulk_natural_oils import basic_url
#from tests.sites.test_bulk_apothecary import basic_url
#from tests.sites.test_mountain_rose_herbs import basic_url
#from tests.sites.test_essential_depot import basic_url
from selbots.sites import *
basic_profile = 'tests/example_profile.json'
basic_penn_profile = 'tests/example_profile_penn.json'

if __name__ == "__main__":
    result = generic_sim(BulkNaturalOils(headless=False), basic_penn_profile, basic_url)
    print_result(result)
