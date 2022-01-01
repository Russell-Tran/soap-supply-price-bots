from tests.helper import *
#from tests.sites.test_wholesale_supplies_plus import basic_url
#from tests.sites.test_scent_sational_supply import basic_url
# from tests.sites.test_nurture_soap import basic_url
from tests.sites.test_brambleberry import basic_url
from selbots.sites import *
basic_profile = 'tests/example_profile.json'

if __name__ == "__main__":
    result = generic_sim(RusticEscentuals(headless=False), basic_profile, "https://www.rusticescentuals.com/products/White-Beeswax-Pastilles-16-ounces.aspx")
    print_result(result)
