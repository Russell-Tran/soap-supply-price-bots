import re
import json
import selbots.common as common

def exactly_one_price(s: str) -> bool:
    return len(re.findall(r'(\$[0-9]+\.[0-9][0-9])', s)) == 1

def generic_sim(b: common.Bot, profile_json: str, product_url: str) -> common.Result:
    with open(profile_json) as file:
        profile = common.Profile(json.load(file))
        b.start()
        try:
            result = b.run(product_url, profile)
        except Exception as e:
            b.stop()
            raise e
        b.stop()
        return result