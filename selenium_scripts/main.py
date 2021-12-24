from sites import *
import json
import time

if __name__ == "__main__":
    print("Hello there Aaron Figgyman")
    with open('profile.json') as file:
        profile = json.load(file)
        product_url = "https://nurturesoap.com/collections/perfect-in-soap-fragrance-oils/products/black-raspberry-vanilla-fragrance-oil"
        shopping_cart_url = "https://nurturesoap.com/cart"
        b = NurtureSoap()
        b.start()
        try:
            result = b.run(product_url, shopping_cart_url, profile)
            print("Subtotal: ", result.subtotal)
            print("Shipping: ", result.shipping)
            print("Total: ", result.total)
            print("Done")

            time.sleep(5)
            b.stop()
        except Exception as e:
            b.stop()
            raise e
