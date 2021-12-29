from tests.helper import *
from tests.sites.test_wholesale_supplies_plus import basic_profile, basic_url
from selbots.sites import *

if __name__ == "__main__":
    print("hi")
    result = generic_sim(WholesaleSuppliesPlus(headless=False), basic_profile, basic_url)
    print_result(result)