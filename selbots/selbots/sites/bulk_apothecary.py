"""
Zap Sourcing 2021
"""
from selbots.common import *

class BulkApothecary(Bot):
    def __init__(self, headless=True):
        super().__init__(shopping_cart_url="https://www.bulkapothecary.com/checkout", headless=headless)

    def run(self, product_url: str, p: Profile):
        d = self.driver
        d.get(product_url)
        
        try:
            # Close the popup
            d.find_element(By.CSS_SELECTOR, ".sumome-react-wysiwyg-outside-horizontal-resize-handles > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)").click()
        except:
            # There way no popup
            pass
            
        d.find_element(By.CSS_SELECTOR, "label.form-label:nth-child(9)").click()
        d.find_element(By.ID, "form-action-addToCart").click()
        time.sleep(1)
        d.get(self.shopping_cart_url)
        time.sleep(0.5)
        d.find_element(By.ID, "email").send_keys(p.email)
        time.sleep(5) # (Failed on 1 second)
        d.find_element(By.ID, "checkout-customer-continue").click()
        time.sleep(5)

        d.find_element(By.ID, "firstNameInput").send_keys(p.first_name)
        d.find_element(By.ID, "lastNameInput").send_keys(p.last_name)
        element = d.find_element(By.ID, "countryCodeInput")
        Select(element).select_by_visible_text(p.country)

        # https://stackoverflow.com/a/44184600/14775744
        elem = d.find_element(By.ID, "postCodeInput")
        elem.send_keys(p.zipcode)
        elem.send_keys(Keys.ARROW_DOWN)
        # Wait for the first dropdown option to appear and open it
        # first_option = WebDriverWait(d, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#ui-id-307")))
        # first_option.send_keys(Keys.RETURN)
        time.sleep(5)
        elem.send_keys(Keys.RETURN)
        
        element = d.find_element(By.ID, "provinceCodeInput")
        Select(element).select_by_visible_text(p.state)
        d.find_element(By.ID, "addressLine1Input").send_keys(p.address)
        d.find_element(By.ID, "companyInput").send_keys(p.company)
        d.find_element(By.ID, "phoneInput").send_keys(p.phone)
        time.sleep(10)

        d.find_element(By.CSS_SELECTOR, "li.form-checklist-item:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(2)").click()
        time.sleep(5)

        cheapest_option = d.find_element(By.CSS_SELECTOR, ".form-checklist-header--selected > div:nth-child(1) > label:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)").text
        cheapest_option = cheapest_option.lower()
        if "customer pickup" in cheapest_option:
            # Don't do customer pickup; do mail order
            d.find_element(By.CSS_SELECTOR, "li.form-checklist-item:nth-child(2) > div:nth-child(1) > div:nth-child(1) > label:nth-child(2)").click()
            time.sleep(5)

        result = Result()
        result.subtotal = d.find_element(By.CSS_SELECTOR, ".cart-priceItem--subtotal > span:nth-child(2) > span:nth-child(1)").text
        result.shipping = d.find_element(By.CSS_SELECTOR, "section.cart-section:nth-child(3) > div:nth-child(2) > div:nth-child(1) > span:nth-child(2) > span:nth-child(1)").text
        result.tax = d.find_element(By.CSS_SELECTOR, "section.cart-section:nth-child(3) > div:nth-child(3) > div:nth-child(1) > span:nth-child(2) > span:nth-child(1)").text
        result.fees = FREE_PRICE
        result.total = d.find_element(By.CSS_SELECTOR, ".cart-priceItem--total > span:nth-child(2) > span:nth-child(1)").text
        return result
