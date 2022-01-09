"""
Zap Sourcing 2021
"""
from selbots.common import *

class ChemistryStore(Bot):
    def __init__(self, headless=True):
        super().__init__(shopping_cart_url="https://www.chemistrystore.com/viewcart.cgi#checkoutformlink", headless=headless)

    def _generate_menu(self) -> Menu:
        d = self.driver
        element = d.find_element(By.ID, "productopts")
        choice_parents = element.find_elements(By.CSS_SELECTOR, 'div.mt10')
        #choice_parents = element.find_elements(By.CSS_SELECTOR, '*')
        choices = []
        choice_texts = []
        for c in choice_parents:
            try:
                #choice = c.find_element(By.XPATH, "//*[contains(text(), '+')]")
                #choice = c.find_element(By.CSS_SELECTOR, "div.mt10:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(3)")
                choice_text = c.find_element(By.CLASS_NAME, "optlinks").text
                #choices.append(choice)
                choice_texts.append(choice_text)
            except Exception as e:
                print (e)
                continue
        print(choice_parents)
        print(choices)
        print(choice_texts)

        choices = choice_parents

        return Menu(choices, choice_texts)

    def run(self, product_url: str, p: Profile, target_qty: pint.quantity.Quantity = None):
        d = self.driver
        d.get(product_url)
        
        # Required minimum $10 so had to go with 2lb option
        # TODO: profile should have boolean commercial address
        time.sleep(3)

        # Menu logic
        menu = self._generate_menu()
        if target_qty:
            element, chosen_qty = menu.choose_element(target_qty)
        else:
            element, chosen_qty = menu.first_viable_element()
        #random_element_to_use_for_scrolling = d.find_element(By.CSS_SELECTOR, ".option-title")
        #d.execute_script('arguments[0].scrollIntoView();', random_element_to_use_for_scrolling)
        
        print(f'chosen qty {chosen_qty}')
        print(f'available quantities {menu.quantities_pretty}')
        #scroll_shim(d, element)
        #time.sleep(3)
        #ActionChains(d).move_to_element(element).click().perform()
        #d.execute_script('arguments[0].scrollIntoView();', element)
        #lement = element.find_element(By.XPATH, "//*[contains(text(), '+')]")
        #ActionChains(d).move_to_element(element).click().perform()
        #element.click()
        #d.find_element(By.CSS_SELECTOR, "div.mt10:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(3)").click()
        
        element.find_element(By.CSS_SELECTOR, ".input-group-addon.plus-option.noselect").click()


        d.find_element(By.ID, "submit-product-w-options").click()
        time.sleep(5)

        d.get(self.shopping_cart_url)
        d.find_element(By.ID, "return_login").click()
        element = d.find_element(By.CSS_SELECTOR, ".customer-account > ol:nth-child(2) > li:nth-child(1) > select:nth-child(2)")
        Select(element).select_by_visible_text("Corporation")
        d.find_element(By.ID, "email").send_keys(p.email)
        time.sleep(3)
        element = d.find_element(By.CSS_SELECTOR, ".billing-address > ol:nth-child(2) > li:nth-child(1) > input:nth-child(2)")
        element.send_keys(p.first_name)
        d.find_element(By.CSS_SELECTOR, ".billing-address > ol:nth-child(2) > li:nth-child(2) > input:nth-child(2)").send_keys(p.last_name)
        d.find_element(By.CSS_SELECTOR, ".billing-address > ol:nth-child(2) > li:nth-child(3) > input:nth-child(2)").send_keys(p.company)
        d.find_element(By.CSS_SELECTOR, ".billing-address > ol:nth-child(2) > li:nth-child(4) > input:nth-child(2)").send_keys(p.address)
        d.find_element(By.CSS_SELECTOR, ".billing-address > ol:nth-child(2) > li:nth-child(6) > input:nth-child(2)").send_keys(p.city)
        element = d.find_element(By.ID, "country")
        Select(element).select_by_visible_text(p.country)
        element = d.find_element(By.CSS_SELECTOR, "#country_fields > li:nth-child(1) > select:nth-child(2)")
        Select(element).select_by_visible_text(p.state)
        d.find_element(By.CSS_SELECTOR, "#country_fields > li:nth-child(2) > input:nth-child(2)").send_keys(p.zipcode)

        # TODO:Is this a commercial address? Clicking by default rn
        # (Notice: move_to_element required to be able to click the checkbox)
        element = d.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/form/div[1]/div[5]/fieldset/ol/li[8]/div/label/input")
        actions = ActionChains(d)
        actions.move_to_element(element).perform()
        element.click()

        d.find_element(By.CSS_SELECTOR, ".billing-address > ol:nth-child(2) > li:nth-child(10) > input:nth-child(2)").send_keys(p.phone)
        d.find_element(By.CSS_SELECTOR, ".billing-address > ol:nth-child(2) > li:nth-child(11) > input:nth-child(2)").send_keys(p.phone)
        d.find_element(By.ID, "calculate_button").click()

        time.sleep(7)
        d.find_element(By.CSS_SELECTOR, "#shipping_data > ol:nth-child(6) > li:nth-child(4) > input:nth-child(1)").click()

        result = Result()
        result.size = chosen_qty
        subtotal = d.find_element(By.CSS_SELECTOR, ".subtotal > span:nth-child(1)").text
        subtotal = re.search('\$[0-9.]+', subtotal).group()   # Returns '$249.99'
        result.subtotal = subtotal
        result.shipping = d.find_element(By.ID, "ShippingCost").text
        result.tax = d.find_element(By.ID, "taxid").text
        result.fees = FREE_PRICE
        result.total = d.find_element(By.ID, "Total").text
        return result
