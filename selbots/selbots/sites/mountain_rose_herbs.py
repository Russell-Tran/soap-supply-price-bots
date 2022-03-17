"""
Zap Sourcing 2021
"""
from selbots.common import *

class MountainRoseHerbs(Bot):
    def __init__(self, headless=True):
        super().__init__(shopping_cart_url="https://mountainroseherbs.com/cart.php", headless=headless)

    def _generate_menu(self) -> Menu:
        d = self.driver
        element = d.find_element(By.CSS_SELECTOR, "div.form-field-control")
        choice_parents = element.find_elements(By.TAG_NAME, 'label')
        choices = []
        choice_texts = []
        for c in choice_parents:
            try:
                choice = c.find_element(By.TAG_NAME, 'input')
                choice_text = c.find_element(By.TAG_NAME, 'span').text
                # (Ensure both find_elements work before appending)
                choices.append(choice)
                choice_texts.append(choice_text)
            except Exception as e:
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
        element.click()

        d.find_element(By.CSS_SELECTOR, "span.product-quantity-toggle:nth-child(1)").click() # Increase qty from 0 to 1
        d.find_element(By.CSS_SELECTOR, "button.button:nth-child(2) > span:nth-child(1)").click()
        time.sleep(3)
        d.get(self.shopping_cart_url)
        d.find_element(By.CSS_SELECTOR, "div.cart-actions:nth-child(8) > a:nth-child(2)").click()
        d.find_element(By.ID, "email").send_keys(p.email)
        d.find_element(By.ID, "checkout-customer-continue").click()
        time.sleep(2)
        d.find_element(By.ID, "firstNameInput").send_keys(p.first_name)
        d.find_element(By.ID, "lastNameInput").send_keys(p.last_name)
        element = d.find_element(By.ID, "postCodeInput")
        element.send_keys(p.zipcode)
        time.sleep(2)
        element.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        element.send_keys(Keys.RETURN)
        time.sleep(1)

        # Sometimes you need this sometimes you don't idk it's pretty shitty
        element = d.find_element(By.ID, "cityInput")
        element.send_keys(" ")

        element = d.find_element(By.ID, "provinceCodeInput")
        Select(element).select_by_visible_text(p.state)
        d.find_element(By.ID, "addressLine1Input").send_keys(p.address)
        d.find_element(By.ID, "phoneInput").send_keys(p.phone)
        time.sleep(15) # Super long but seems like otherwise you get nondeterministic behavior, eg. can't find the tax element
        
        result = Result()
        result.size = chosen_qty
        result.subtotal = d.find_element(By.CSS_SELECTOR, ".product-price").text
        result.shipping = d.find_element(By.CSS_SELECTOR, "section.cart-section:nth-child(3) > div:nth-child(2) > div:nth-child(1) > span:nth-child(2) > span:nth-child(1)").text
        try:
            result.tax = d.find_element(By.CSS_SELECTOR, ".changeHighlight-enter-done > span:nth-child(2) > span:nth-child(1)").text
        except:
            result.tax = d.find_element(By.CSS_SELECTOR, "section.cart-section:nth-child(3) > div:nth-child(3) > div:nth-child(1) > span:nth-child(2) > span:nth-child(1)").text
        result.fees = FREE_PRICE
        result.total = d.find_element(By.CSS_SELECTOR, ".cart-priceItem--total > span:nth-child(2) > span:nth-child(1)").text
        return result
