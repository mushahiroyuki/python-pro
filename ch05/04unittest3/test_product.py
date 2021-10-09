import unittest 

from product import Product 

class ProductTestCase(unittest.TestCase): 
    def test_transform_name_for_sku(self): 
        small_black_shoes = Product('shoes', 'S', 'black') 
        expected_value = 'SHOES'  # 期待される値
        actual_value = small_black_shoes.transform_name_for_sku()  # 実際の値
        self.assertEqual(expected_value, actual_value)
