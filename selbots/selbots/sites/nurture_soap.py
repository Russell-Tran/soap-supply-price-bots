"""
Zap Sourcing 2021
"""
from selbots.common import *

class NurtureSoap(Bot):
    def __init__(self, headless=True):
        super().__init__(shopping_cart_url="https://nurturesoap.com/cart", headless=headless)

    def run(self, product_url: str, p: Profile):
        d = self.driver
        shopping_cart_url = self.shopping_cart_url
        d.get(product_url)
        
        time.sleep(2)
        d.find_element(By.CSS_SELECTOR, "button.product-form__add-button").click()
        time.sleep(2)
        d.get(shopping_cart_url)
        time.sleep(4)
        d.find_element(By.CSS_SELECTOR, ".cart-recap__checkout").click()
        d.find_element(By.ID, "checkout_email").send_keys(p.email)
        d.find_element(By.ID, "checkout_shipping_address_first_name").send_keys(p.first_name)
        d.find_element(By.ID, "checkout_shipping_address_last_name").send_keys(p.last_name)
        d.find_element(By.ID, "checkout_shipping_address_address1").send_keys(p.address)
        d.find_element(By.ID, "checkout_shipping_address_city").send_keys(p.city)
        element = d.find_element(By.ID, "checkout_shipping_address_country")
        Select(element).select_by_visible_text(p.country)
        element = d.find_element(By.ID, "checkout_shipping_address_province")
        Select(element).select_by_visible_text(p.state)
        d.find_element(By.ID, "checkout_shipping_address_zip").send_keys(p.zipcode)
        d.find_element(By.ID, "checkout_shipping_address_phone").send_keys(p.phone)
        d.find_element(By.ID, "continue_button").click()
        time.sleep(7)

        result = Result()
        result.subtotal = d.find_element(By.CSS_SELECTOR, ".total-line--subtotal > td:nth-child(2) > span:nth-child(1)").text
        result.shipping = d.find_element(By.CSS_SELECTOR, "tr.total-line:nth-child(2) > td:nth-child(2) > span:nth-child(1)").text
        result.tax = d.find_element(By.CSS_SELECTOR, "tr.total-line:nth-child(3) > td:nth-child(2) > span:nth-child(1)").text
        result.fees = FREE_PRICE
        result.total = d.find_element(By.CSS_SELECTOR, ".payment-due__price").text
        return result
