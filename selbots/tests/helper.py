import re
import json
import selbots.common as common
import pint

def exactly_one_price(s: str) -> bool:
    if not s:
        return False
    return len(re.findall(r'(\$[0-9]+\.[0-9][0-9])', s)) == 1

def exactly_one_price_assertions(result: common.Result):
    assert exactly_one_price(result.subtotal)
    assert exactly_one_price(result.tax)
    assert exactly_one_price(result.fees)
    assert exactly_one_price(result.shipping)
    assert exactly_one_price(result.total)

def generic_sim(b: common.Bot, profile_json: str, product_url: str) -> common.Result:
    with open(profile_json) as file:
        profile = common.Profile(json.load(file))
        b.start()
        try:
            result = b.run(product_url, profile)
        except Exception as e:
            if b.headless:
                b.stop()
            raise e
        if b.headless:
            b.stop()
        return result

# Upgrade for considering target qty
def generic_sim_qty(b: common.Bot, profile_json: str, product_url: str, 
    target_qty: str) -> common.Result:
    
    target_qty = common.extract_quantity(target_qty)
    with open(profile_json) as file:
        profile = common.Profile(json.load(file))
        b.start()
        try:
            result = b.run(product_url, profile, target_qty)
        except Exception as e:
            if b.headless:
                b.stop()
            raise e
        if b.headless:
            b.stop()
        return result

def print_result(result: common.Result):
    print("Size:     ", result.size)
    print("Subtotal: ", result.subtotal)
    print("Fees:     ", result.fees)
    print("Tax:      ", result.tax)
    print("Shipping: ", result.shipping)
    print("Total:    ", result.total)