import json
from selbots.common import *

def test_profile():
    with open('tests/example_profile.json') as file:
        profile = Profile(json.load(file))
        assert profile.first_name == "John"
        assert profile.last_name == "Snow"
        assert profile.email == "winteriscoming@gmail.com"
        assert profile.phone == "(949) 361-8200"
        assert profile.fax == "(949) 493-8729"
        assert profile.company == "Cool Soap, Inc."
        assert profile.address == "15 Calle Loyola"
        assert profile.address_2 == "Suite #15"
        assert profile.city == "San Clemente"
        assert profile.state == "California"
        assert profile.country == "United States"
        assert profile.zipcode == "92673"
