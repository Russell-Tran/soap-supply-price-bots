from selbots.common import Bot
from selbots.sites import *

def pick(url: str) -> Bot:
    url = url.lower()
    if "brambleberry.com" in url:
        return Brambleberry()
    elif "bulkapothecary.com" in url:
        return BulkApothecary()
    elif "bulknaturaloils.com" in url:
        return BulkNaturalOils()
    elif "chemistrystore.com" in url:
        return ChemistryStore()
    elif "myfortune3cart.com" in url: # TEMPORARY PATCH FOR THE FACT THAT CHEMISTRY STORE USES THIS ALTERNATE URL TOO
        return ChemistryStore() 
    elif "essentialdepot.com" in url:
        return EssentialDepot()
    elif "mountainroseherbs.com" in url:
        return MountainRoseHerbs()
    elif "nurturesoap.com" in url:
        return NurtureSoap()
    elif "rusticescentuals.com" in url:
        return RusticEscentuals()
    elif "scentsationalsupply.com" in url:
        return ScentSationalSupply()
    elif "wholesalesuppliesplus.com" in url:
        return WholesaleSuppliesPlus()
    else:
        return None