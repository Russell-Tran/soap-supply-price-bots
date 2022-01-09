"""
Zap Sourcing 2021
"""
from selbots.common import *

class ScentSationalSupply(Bot):
    def __init__(self, headless=True):
        super().__init__(shopping_cart_url=None, headless=headless)

    def _generate_menu(self) -> Menu:
        d = self.driver
        element = d.find_element(By.CSS_SELECTOR, ".col-sm-10")
        choice_parents = element.find_elements(By.TAG_NAME, 'label')
        choices = []
        choice_texts = []
        for c in choice_parents:
            try:
                choice = c.find_element(By.TAG_NAME, 'input')
                choice_text = c.text
                # (Ensure both find_elements work before appending)
                choices.append(choice)
                choice_texts.append(choice_text)
            except Exception as e:
                continue
        return Menu(choices, choice_texts)

    def run(self, product_url: str, p: Profile, target_qty: pint.quantity.Quantity = None):
        d = self.driver
        shopping_cart_url = self.shopping_cart_url
        d.get(product_url)
        
        # Menu logic
        menu = self._generate_menu()
        if target_qty:
            element, chosen_qty = menu.choose_element(target_qty)
        else:
            element, chosen_qty = menu.first_viable_element()
        ActionChains(d).move_to_element(element).click().perform()

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
        result.size = chosen_qty
        result.subtotal = d.find_element(By.CSS_SELECTOR, ".sidewidt > table:nth-child(5) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > span:nth-child(1)").text
        result.shipping = d.find_element(By.CSS_SELECTOR, ".sidewidt > table:nth-child(5) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > span:nth-child(1)").text
        result.fees = FREE_PRICE
        result.tax = FREE_PRICE
        result.total = d.find_element(By.CSS_SELECTOR, ".sidewidt > table:nth-child(5) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > span:nth-child(1)").text
        return result
