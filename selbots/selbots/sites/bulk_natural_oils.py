"""
Zap Sourcing 2021
"""
from selbots.common import *

class BulkNaturalOils(Bot):
    def __init__(self, headless=True):
        super().__init__(shopping_cart_url=None, headless=headless)

    def run(self, product_url: str, p: Profile):
        d = self.driver
        d.get(product_url)

        element = d.find_elements(By.ID, "selectqty")[0]
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
        result.subtotal = d.find_element(By.CSS_SELECTOR, "tr.totals:nth-child(1) > td:nth-child(2) > span:nth-child(1)").text
        result.shipping = d.find_element(By.CSS_SELECTOR, "tr.totals:nth-child(2) > td:nth-child(2) > span:nth-child(1)").text
        result.fees = FREE_PRICE
        result.tax = FREE_PRICE
        result.total = d.find_element(By.CSS_SELECTOR, ".grand > td:nth-child(2) > strong:nth-child(1) > span:nth-child(1)").text
        return result
