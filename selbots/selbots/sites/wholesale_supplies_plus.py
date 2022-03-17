from selbots.common import *

class WholesaleSuppliesPlus(Bot):
    def __init__(self, headless=True):
        super().__init__(shopping_cart_url="https://www.wholesalesuppliesplus.com/securessl/checkout.aspx", headless=headless)

    def _generate_menu(self) -> Menu:
        d = self.driver
        element = d.find_element(By.CSS_SELECTOR, "#Buy > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1)")
        choices = element.find_elements(By.TAG_NAME, 'input')
        choice_texts = element.text.split('\n')
        print(f"DEBUG: choices = {choices}, choice_texts = {choice_texts}")
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

        d.find_element(By.ID, "MainContent_ChildContent_ParentData_btnAddToCart_0").click()
        # Checkout
        d.get(shopping_cart_url)

        # Fill out checkout details
        d.find_element(By.ID, "MainContent_txtBillFirstNameNew").click()
        d.find_element(By.ID, "MainContent_txtBillFirstNameNew").click()
        element = d.find_element(By.ID, "MainContent_txtBillFirstNameNew")
        actions = ActionChains(d)
        actions.double_click(element).perform()
        d.find_element(By.ID, "MainContent_txtBillFirstNameNew").send_keys(p.first_name)
        d.find_element(By.ID, "MainContent_txtBillLastNameNew").click()
        d.find_element(By.ID, "MainContent_txtBillLastNameNew").send_keys(p.last_name)
        d.find_element(By.ID, "MainContent_txtBillCompanyNameNew").click()
        d.find_element(By.ID, "MainContent_txtBillCompanyNameNew").send_keys(p.company)
        d.find_element(By.ID, "MainContent_txtBillAddr1New").click()
        d.find_element(By.ID, "MainContent_txtBillAddr1New").send_keys(p.address)
        d.find_element(By.ID, "MainContent_txtBillCityNew").click()
        d.find_element(By.ID, "MainContent_txtBillCityNew").send_keys(p.city)
        d.find_element(By.ID, "MainContent_cmbBillStateProvinceNew").click()
        dropdown = d.find_element(By.ID, "MainContent_cmbBillStateProvinceNew")
        dropdown.find_element(By.XPATH, f"//option[. = '{p.state}']").click()
        d.find_element(By.CSS_SELECTOR, "#MainContent_cmbBillStateProvinceNew > option:nth-child(9)").click()
        d.find_element(By.ID, "MainContent_txtBillPostalCodeNew").click()
        d.find_element(By.ID, "MainContent_txtBillPostalCodeNew").send_keys(p.zipcode)
        d.find_element(By.ID, "MainContent_txtBillEmailNew").click()
        time.sleep(1)
        d.find_element(By.ID, "MainContent_txtBillEmailNew").send_keys(p.email)
        time.sleep(1)
        d.find_element(By.ID, "MainContent_txtBillPhoneNew").click()
        time.sleep(1)
        d.find_element(By.ID, "MainContent_txtBillPhoneNew").send_keys(p.phone)
        time.sleep(1)
        d.find_element(By.ID, "MainContent_txtShipFirstNameNew").click()
        d.find_element(By.ID, "MainContent_txtShipFirstNameNew").send_keys(p.first_name)
        d.find_element(By.ID, "MainContent_txtShipLastNameNew").send_keys(p.last_name)
        d.find_element(By.ID, "MainContent_txtShipCompanyNameNew").click()
        d.find_element(By.ID, "MainContent_txtShipCompanyNameNew").send_keys(p.company)
        d.find_element(By.ID, "MainContent_txtShipAddr1New").click()
        d.find_element(By.ID, "MainContent_txtShipAddr1New").send_keys(p.address)
        d.find_element(By.ID, "MainContent_txtShipCityNew").click()
        d.find_element(By.ID, "MainContent_txtShipCityNew").send_keys(p.city)
        d.find_element(By.ID, "MainContent_cmbShipStateProvinceNew").click()
        dropdown = d.find_element(By.ID, "MainContent_cmbShipStateProvinceNew")
        dropdown.find_element(By.XPATH, f"//option[. = '{p.state}']").click()
        d.find_element(By.CSS_SELECTOR, "#MainContent_cmbShipStateProvinceNew > option:nth-child(9)").click()
        d.find_element(By.ID, "MainContent_txtShipPostalCodeNew").click()
        d.find_element(By.ID, "MainContent_txtShipPostalCodeNew").send_keys(p.zipcode)
        d.find_element(By.ID, "MainContent_txtShipEmailNew").click()
        time.sleep(1)
        d.find_element(By.ID, "MainContent_txtShipEmailNew").send_keys(p.email)
        time.sleep(1)
        d.find_element(By.ID, "MainContent_txtShipPhoneNew").click()
        time.sleep(1)
        d.find_element(By.ID, "MainContent_txtShipPhoneNew").send_keys(p.phone)
        time.sleep(1)
        d.find_element(By.CSS_SELECTOR, ".co-forms:nth-child(1)").click()
        d.find_element(By.ID, "MainContent_btnUpdateBillingShippingNew").click()
        d.find_element(By.CSS_SELECTOR, "#MainContent_pnlSubmitOrder > div").click()
        d.find_element(By.CSS_SELECTOR, "#MainContent_pnlSubmitOrder > div").click()
        
        result = Result()
        result.size = chosen_qty
        result.subtotal = d.find_element(By.ID, "MainContent_lblSubTotal").text
        result.shipping = d.find_element(By.ID, "MainContent_lblShipCost").text
        result.fees = d.find_element(By.ID, "MainContent_lblHandlingFee").text
        result.tax = d.find_element(By.ID, "MainContent_lblTaxAmount").text
        result.total = d.find_element(By.ID, "MainContent_lblGrandTotal").text
        return result
