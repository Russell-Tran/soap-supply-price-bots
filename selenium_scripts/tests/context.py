import os
import sys
import re
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import bot
import sites

def exactly_one_price(s: str):
    return len(re.findall(r'(\$[0-9]+\.[0-9][0-9])', s)) == 1