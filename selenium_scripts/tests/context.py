import os
import sys
import re
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import bot
import sites

def exactly_one_price(s: str) -> bool:
    return len(re.findall(r'(\$[0-9]+\.[0-9][0-9])', s)) == 1

def generic_sim(b: bot.Bot, profile_json: str, product_url: str) -> bot.Result:
    with open(profile_json) as file:
        profile = bot.Profile(json.load(file))
        b.start()
        try:
            result = b.run(product_url, profile)
        except Exception as e:
            b.stop()
            raise e
        b.stop()
        return result