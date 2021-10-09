# ch05/04unittest3/test_product.py
import unittest 

from product import Product 

class ProductTestCase(unittest.TestCase): 
    def test_transform_name_for_sku(self): 
        small_black_shoes = Product('shoes', 'S', 'black') 
        expected_value = 'SHOEZ'
        actual_value = small_black_shoes.transform_name_for_sku() 
        self.assertEqual(expected_value, actual_value)
