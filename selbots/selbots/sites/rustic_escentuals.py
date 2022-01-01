"""
INCOMPLETE DUE TO CLOUDFLARE CAPTCHA 
TODO: INVESTIGATE USING CHROME INSTEAD https://stackoverflow.com/a/64590951/14775744

"""
"""
Zap Sourcing 2021
"""
from selbots.common import *

class RusticEscentuals(Bot):
    def __init__(self, headless=True):
        super().__init__(shopping_cart_url="https://www.rusticescentuals.com/shoppingcart.aspx", headless=headless)

    def run(self, product_url: str, p: Profile):
        d = self.driver
        d.get(product_url)

        time.sleep(3)
        d.find_elements(By.ID, "ProductPriceIDText")[1].click()
        time.sleep(20)
        d.find_element(By.ID, "MainContent_ChildContent_ParentData_btnAddToCart_0").click()
        """
        print("C")
        time.sleep(30)
        d.get(shopping_cart_url)
        print("D")
        time.sleep(10)
        d.find_element(By.ID, "MainContent_btnCheckoutGuest").click()
        print("E")
        time.sleep(10)
        d.find_element(By.ID, "MainContent_txtBillFirstNameNew").send_keys(p['shipping_address']['first_name'])
        d.find_element(By.ID, "MainContent_txtBillLastNameNew").send_keys(p['shipping_address']['last_name'])
        d.find_element(By.ID, "MainContent_txtBillAddr1New").send_keys(p['shipping_address']['address'])
        d.find_element(By.ID, "MainContent_txtBillAddr2New").send_keys(p['shipping_address']['address_2'])
        d.find_element(By.ID, "MainContent_txtBillCityNew").send_keys(p['shipping_address']['city'])
        element = d.find_element(By.ID, "MainContent_cmbBillStateProvinceNew")
        Select(element).select_by_visible_text(p['shipping_address']['state'])
        d.find_element(By.ID, "MainContent_txtBillPostalCodeNew").send_keys(p['shipping_addresss']['zipcode'])
        d.find_element(By.ID, "MainContent_txtBillEmailNew").send_keys(p['shipping_addresss']['email'])
        d.find_element(By.ID, "MainContent_txtBillPhoneNew").send_keys(p['shipping_addresss']['phone'])
        d.find_element(By.ID, "MainContent_chkShipToBilling").click()
        time.sleep(1)
        d.find_element(By.ID, "MainContent_btnUpdateBillingShippingNew").click()
        time.sleep(1)

        subtotal = d.find_element(By.ID, "MainContent_lblSubTotal").text
        shipping = d.find_element(By.ID, "MainContent_lblShipCost").text
        coupons = d.find_element(By.ID, "MainContent_lblDiscount").text
        tax = d.find_element(By.ID, "MainContent_lblTaxAmount").text
        total = d.find_element(By.ID, "MainContent_lblGrandTotal").text

        print("Subtotal: ", subtotal)
        print("Shipping: ", shipping)
        print("Tax: ", tax)
        print("Total: ", total)
        print("Done")
        time.sleep(5)
        
        self.stop()
        """
