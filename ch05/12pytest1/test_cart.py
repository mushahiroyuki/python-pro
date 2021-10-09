# ch05/08tryitout1/test_cart.py
import unittest

from cart import ShoppingCart
from product import Product

# Full test suite for product and shopping cart
class ProductTestCase(unittest.TestCase):
#@@range_begin(list2)  # ←この行は無視してください    
# ch05/08tryitout/test_cart.py    
#@@range_begin(list1)  # ←この行は無視してください
    def test_transform_name_for_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        self.assertEqual(
            'SHOES',
            small_black_shoes.transform_name_for_sku(),
        )
#@@range_end(list1)  # ←この行は無視してください
    def test_transform_color_for_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        self.assertEqual(
            'BLACK',
            small_black_shoes.transform_color_for_sku(),
        )

    def test_generate_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        self.assertEqual(
            'SHOES-S-BLACK',
            small_black_shoes.generate_sku(),
        )


class ShoppingCartTestCase(unittest.TestCase):
    def test_cart_initially_empty(self):
        cart = ShoppingCart()
        self.assertDictEqual({}, cart.products)

    def test_add_product(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'blue')

        cart.add_product(product)

        self.assertDictEqual({'SHOES-S-BLUE': {'quantity': 1}}, cart.products)

    def test_add_two_of_a_product(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'blue')

        cart.add_product(product, quantity=2)

        self.assertDictEqual({'SHOES-S-BLUE': {'quantity': 2}}, cart.products)

    def test_add_two_different_products(self):
        cart = ShoppingCart()
        product_one = Product('shoes', 'S', 'blue')
        product_two = Product('shirt', 'M', 'gray')

        cart.add_product(product_one)
        cart.add_product(product_two)

        self.assertDictEqual(
            {
                'SHOES-S-BLUE': {'quantity': 1},
                'SHIRT-M-GRAY': {'quantity': 1}
            },
            cart.products
        )

    def test_add_and_remove_product(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'blue')

        cart.add_product(product)
        cart.remove_product(product)

        self.assertDictEqual({}, cart.products)

    def test_remove_too_many_products(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'blue')

        cart.add_product(product)
        cart.remove_product(product, quantity=2)  # ←失敗する

        self.assertDictEqual({}, cart.products)
#@@range_end(list2)  # ←この行は無視してください    
