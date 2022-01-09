"""
Zap Sourcing 2021
"""
from selbots.common import *

class EssentialDepot(Bot):
    def __init__(self, headless=True):
        super().__init__(shopping_cart_url=None, headless=headless)

    def run(self, product_url: str, p: Profile, target_qty: pint.quantity.Quantity = None):
        d = self.driver
        shopping_cart_url = self.shopping_cart_url
        d.get(product_url)

        # For this website, each quantity has its own page, so no need for a menu
        chosen_qty = extract_quantity_nonbase(d.find_element(By.CSS_SELECTOR, "h1.column").text)

        d.find_element(By.ID, "js-add-to-cart").click()
        d.find_element(By.ID, "js-mini-basket").click()

        time.sleep(3)
        element = d.find_element(By.XPATH, "/html/body/div[3]/header/div[2]/div[3]/div[1]/div[3]/a")
        d.execute_script("arguments[0].click();", element)

        time.sleep(3)
        d.find_element(By.LINK_TEXT, "Continue as a Guest").click()
        
        time.sleep(3)
        d.find_element(By.ID, "js-billing-to-show").click()

        # Enter shipping info
        d.find_element(By.ID, "l-ShipFirstName").send_keys(p.first_name)
        d.find_element(By.ID, "l-ShipLastName").send_keys(p.last_name)
        d.find_element(By.ID, "l-ShipEmail").send_keys(p.email)
        d.find_element(By.ID, "l-ShipPhone").send_keys(p.phone)
        d.find_element(By.ID, "l-ShipFax").send_keys(p.fax)
        d.find_element(By.ID, "l-ShipCompany").send_keys(p.company)
        d.find_element(By.ID, "l-ShipAddress1").send_keys(p.address)
        d.find_element(By.ID, "l-ShipCity").send_keys(p.city)
        element = d.find_element(By.ID, "ShipStateSelect")
        Select(element).select_by_visible_text(p.state)
        d.find_element(By.ID, "l-ShipZip").send_keys(p.zipcode)
        element = d.find_element(By.ID, "ShipCountry")
        Select(element).select_by_visible_text(p.country)

        # Enter billing info
        d.find_element(By.ID, "l-BillFirstName").send_keys(p.first_name)
        d.find_element(By.ID, "l-BillLastName").send_keys(p.last_name)
        d.find_element(By.ID, "l-BillEmail").send_keys(p.email)
        d.find_element(By.ID, "l-BillPhone").send_keys(p.phone)
        d.find_element(By.ID, "l-BillFax").send_keys(p.fax)
        d.find_element(By.ID, "l-BillCompany").send_keys(p.company)
        d.find_element(By.ID, "l-BillAddress1").send_keys(p.address)
        d.find_element(By.ID, "l-BillCity").send_keys(p.city)
        element = d.find_element(By.ID, "BillStateSelect")
        Select(element).select_by_visible_text(p.state)
        d.find_element(By.ID, "l-BillZip").send_keys(p.zipcode)
        element = d.find_element(By.ID, "BillCountry")
        Select(element).select_by_visible_text(p.country)
        
        d.find_element(By.CSS_SELECTOR, "input.bg-red").click() # "Continue to Shipping/Payment"
        time.sleep(3)

        result = Result()
        result.size = chosen_qty
        result.subtotal = d.find_element(By.CSS_SELECTOR, "strong.column:nth-child(2)").text

        d.find_element(By.CSS_SELECTOR, "input.button:nth-child(2)").click() # "Continue to Payment Info"
        time.sleep(3)
        result.shipping = d.find_element(By.CSS_SELECTOR, "p.whole:nth-child(2) > span:nth-child(2)").text
        result.tax = d.find_element(By.CSS_SELECTOR, "p.whole:nth-child(3) > span:nth-child(2)").text
        result.fees = FREE_PRICE
        result.total = d.find_element(By.CSS_SELECTOR, "p.column:nth-child(4) > strong:nth-child(2)").text
        return result
