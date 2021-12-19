from nurture_soap import *

if __name__ == "__main__":
    print("Hello there Aaron Figgyman")
    with open('profile.json') as file:
        profile = json.load(file)
        product_url = "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/eucalyptus-mint-fragrance-oil-fragrance-oil"
        shopping_cart_url = "https://nurturesoap.com/cart"
        b = NurtureSoap()
        b.run(product_url, shopping_cart_url, profile)