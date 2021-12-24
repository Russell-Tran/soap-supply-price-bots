"""
Zap Sourcing 2021
"""
from bot import *

class NurtureSoap(Bot):
    def run(self, product_url, shopping_cart_url, p):
        d = self.driver
        d.get(product_url)
        time.sleep(3)
        d.find_element(By.CSS_SELECTOR, "button.product-form__add-button").click()
        time.sleep(3)
        d.get(shopping_cart_url)
        time.sleep(3)
        d.find_element(By.CSS_SELECTOR, ".cart-recap__checkout").click()
        d.find_element(By.ID, "checkout_email").send_keys(p['shipping_address']['email'])
        d.find_element(By.ID, "checkout_shipping_address_first_name").send_keys(p['shipping_address']['email'])
        d.find_element(By.ID, "checkout_shipping_address_last_name").send_keys(p['shipping_address']['email'])
        d.find_element(By.ID, "checkout_shipping_address_address1").send_keys(p['shipping_address']['email'])
        d.find_element(By.ID, "checkout_shipping_address_city").send_keys(p['shipping_address']['email'])
        element = d.find_element(By.ID, "checkout_shipping_address_country")
        Select(element).select_by_visible_text(p['shipping_address']['country'])
        element = d.find_element(By.ID, "checkout_shipping_address_province")
        Select(element).select_by_visible_text(p['shipping_address']['state'])
        d.find_element(By.ID, "checkout_shipping_address_zip").send_keys(p['shipping_address']['zipcode'])
        d.find_element(By.ID, "checkout_shipping_address_phone").send_keys(p['shipping_address']['phone'])
        d.find_element(By.ID, "continue_button").click()
        time.sleep(5)

        result = Result()
        result.subtotal = d.find_element(By.CSS_SELECTOR, ".total-line--subtotal > td:nth-child(2) > span:nth-child(1)").text
        result.shipping = d.find_element(By.CSS_SELECTOR, "tr.total-line:nth-child(2) > td:nth-child(2) > span:nth-child(1)").text
        result.total = d.find_element(By.CSS_SELECTOR, ".payment-due__price").text
        return result
