import unittest

from cart import ShoppingCart
from product import Product

class ShoppingCartTestCase(unittest.TestCase):  # <1>
    def test_add_and_remove_product(self):
        cart = ShoppingCart()  # <2>
        product = Product('shoes', 'S', 'blue')  # <3>

        cart.add_product(product)  # <4>
        cart.remove_product(product)  # <5>

        self.assertDictEqual({}, cart.products)  # <6>
