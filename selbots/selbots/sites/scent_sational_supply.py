"""
Zap Sourcing 2021
"""
from selbots.common import *

class ScentSationalSupply(Bot):
    def __init__(self):
        super().__init__(shopping_cart_url=None)

    def run(self, product_url: str, p: Profile):
        d = self.driver
        shopping_cart_url = self.shopping_cart_url
        d.get(product_url)
        
        d.find_element(By.ID, "option6891808").click() # third option, the 1lb option for titanium
        d.find_element(By.CLASS_NAME, "cart").click()
        time.sleep(3)
        d.find_element(By.ID, "cart_checkout1").click()
        time.sleep(3)
        d.find_element(By.ID, "accountFrm_accountguest").click()
        d.find_element(By.CSS_SELECTOR, "button.btn:nth-child(4)").click()

        d.find_element(By.ID, "guestFrm_firstname").send_keys(p.first_name)
        d.find_element(By.ID, "guestFrm_lastname").send_keys(p.last_name)
        d.find_element(By.ID, "guestFrm_email").send_keys(p.email)
        d.find_element(By.ID, "guestFrm_address_1").send_keys(p.address)
        d.find_element(By.ID, "guestFrm_city").send_keys(p.city)
        element = d.find_element(By.ID, "guestFrm_zone_id")
        Select(element).select_by_visible_text(p.state)
        d.find_element(By.ID, "guestFrm_postcode").send_keys(p.zipcode)
        element = d.find_element(By.ID, "guestFrm_country_id")
        Select(element).select_by_visible_text(p.country)
        d.find_element(By.CSS_SELECTOR, "button.pull-right").click()

        d.find_element(By.ID, "guest_default_weightdefault_weight_1default_weight.default_weight_1").click()
        d.find_element(By.ID, "guest_payment_methoddefault_pp_standart").click()
        d.find_element(By.CSS_SELECTOR, "button.btn:nth-child(2)").click()

        result = Result()
        result.subtotal = d.find_element(By.CSS_SELECTOR, ".sidewidt > table:nth-child(5) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > span:nth-child(1)").text
        result.shipping = d.find_element(By.CSS_SELECTOR, ".sidewidt > table:nth-child(5) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > span:nth-child(1)").text
        result.total = d.find_element(By.CSS_SELECTOR, ".sidewidt > table:nth-child(5) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > span:nth-child(1)").text
        return result

        

if __name__ == "__main__":
    with open('profile.json') as file:
        profile = json.load(file)
        product_url = "https://scentsationalsupply.com/additives-for-soapmaking/water-soluble-titanium-dioxide"
        shopping_cart_url = None
        b = ScentSationalSupply()
        b.run(product_url, shopping_cart_url, profile)

