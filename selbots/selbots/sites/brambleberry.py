"""
Zap Sourcing 2021
"""
from selenium.webdriver.common import by
from selbots.common import *

class Brambleberry(Bot):
    def __init__(self, headless=True):
        super().__init__(shopping_cart_url="https://www.brambleberry.com/shoppingbag", headless=headless)

    def run(self, product_url: str, p: Profile):
        # self._dev(product_url, p)
        # return

        d = self.driver
        shopping_cart_url = self.shopping_cart_url
        d.get(product_url)

        # https://stackoverflow.com/a/37303115/14775744
        timeout = 5
        element_present = EC.presence_of_element_located((By.ID, "CybotCookiebotDialogBodyUnderlay"))
        WebDriverWait(d, timeout).until(element_present)

        # Cookie
        time.sleep(3)
        d.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
        time.sleep(3)

        #d.find_element(By.LINK_TEXT, "5 lbs").click()
        time.sleep(1)
        d.find_element(By.ID, "add-to-cart").click()
        d.get(shopping_cart_url)
        time.sleep(2)

        # https://stackoverflow.com/a/63157469/14775744
        # https://stackoverflow.com/questions/41857614/how-to-find-xpath-of-an-element-in-firefox-inspector
        xpath = "/html/body/div[1]/div[3]/div/div[2]/div[2]/form/div/div[1]/table/tbody/tr[5]/td[1]/table/tbody/tr[1]/td/a"
        element = d.find_element(By.XPATH, xpath)
        d.execute_script("arguments[0].click();", element)

        d.find_element(By.ID, "dwfrm_shippingestimator_shippingestimate_zipcode").click()
        d.find_element(By.ID, "dwfrm_shippingestimator_shippingestimate_zipcode").send_keys("92673")
        time.sleep(1)
        d.find_element(By.NAME, "dwfrm_cart_estimate").click()
        time.sleep(2)

        result = Result()
        result.subtotal = d.find_element(By.CSS_SELECTOR, ".order-subitems > td:nth-child(2)").text
        result.fees = FREE_PRICE
        result.shipping = d.find_element(By.CSS_SELECTOR, ".order-shipping > .align-right").text
        result.tax = d.find_element(By.CSS_SELECTOR, ".order-sales-tax > td:nth-child(2)").text
        result.total = d.find_element(By.CSS_SELECTOR, ".order-value").text
        return result

    def _dev(self, product_url: str, p: Profile):
        d = self.driver
        shopping_cart_url = self.shopping_cart_url
        d.get(product_url)

        # https://stackoverflow.com/a/37303115/14775744
        timeout = 5
        element_present = EC.presence_of_element_located((By.ID, "CybotCookiebotDialogBodyUnderlay"))
        WebDriverWait(d, timeout).until(element_present)

        # Cookie
        time.sleep(3)
        d.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
        time.sleep(3)

        element = d.find_element(By.CSS_SELECTOR, ".swatches")
        choices = element.find_elements(By.CLASS_NAME, "selectable")
        choices_deeper = []
        for choice in choices:
            try:
                choices_deeper.append(choice.find_element(By.TAG_NAME, 'a'))
            except:
                continue
        choice_texts = [c.text for c in choices_deeper]
        
        print(choice_texts)
        choices_deeper[3].click()