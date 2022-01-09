"""
Zap Sourcing 2021
"""
from selbots.common import *

class BulkNaturalOils(Bot):
    def __init__(self, headless=True):
        super().__init__(shopping_cart_url=None, headless=headless)

    def _generate_menu(self) -> Menu:
        d = self.driver
        element = d.find_element(By.CSS_SELECTOR, "#super-product-table > tbody:nth-child(3)")
        choice_parents = element.find_elements(By.TAG_NAME, 'tr')
        choices = []
        choice_texts = []
        for c in choice_parents:
            try:
                choice = c.find_element(By.ID, "selectqty") 
                choice_text = c.find_element(By.TAG_NAME, 'a').text
                choices.append(choice)
                choice_texts.append(choice_text)
            except:
                continue
        return Menu(choices, choice_texts)

    def run(self, product_url: str, p: Profile, target_qty: pint.quantity.Quantity = None):
        d = self.driver
        d.get(product_url)

        # Menu logic
        menu = self._generate_menu()
        if target_qty:
            element, chosen_qty = menu.choose_element(target_qty)
        else:
            element, chosen_qty = menu.first_viable_element()
        Select(element).select_by_visible_text("1")
        
        element = d.find_element(By.ID, "product-addtocart-button")
        scroll_shim(d, element)
        ActionChains(d).move_to_element(element).click().perform() # https://stackoverflow.com/a/49261182/14775744
        time.sleep(10)
        element = d.find_element(By.CSS_SELECTOR, "div.field:nth-child(4) > div:nth-child(2)").find_element(By.CLASS_NAME, "select")
        Select(element).select_by_visible_text(p.country)
        element = d.find_element(By.CSS_SELECTOR, "div.field:nth-child(5) > div:nth-child(2)").find_element(By.CLASS_NAME, "select")
        Select(element).select_by_visible_text(p.state)
        element = d.find_element(By.CSS_SELECTOR, "div.field:nth-child(7) > div:nth-child(2)").find_element(By.CLASS_NAME, "input-text")
        element.send_keys(p.zipcode)
        time.sleep(5)
        try:
            d.find_element(By.ID, "s_method_fedexups_fedex_ground_home_delivery").click()
        except:
            d.find_element(By.ID, "s_method_fedexups_ups_03").click()
        time.sleep(5)

        result = Result()
        result.size = chosen_qty
        result.subtotal = d.find_element(By.CSS_SELECTOR, "tr.totals:nth-child(1) > td:nth-child(2) > span:nth-child(1)").text
        result.shipping = d.find_element(By.CSS_SELECTOR, "tr.totals:nth-child(2) > td:nth-child(2) > span:nth-child(1)").text
        result.fees = FREE_PRICE
        result.tax = FREE_PRICE
        result.total = d.find_element(By.CSS_SELECTOR, ".grand > td:nth-child(2) > strong:nth-child(1) > span:nth-child(1)").text
        return result
