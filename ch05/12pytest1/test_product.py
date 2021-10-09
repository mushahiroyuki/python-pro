import unittest

from product import Product


class ProductTestCase(unittest.TestCase):

    def test_transform_name_for_sku(self): 
        small_black_shoes = Product('shoes', 'S', 'black')
        self.assertEqual(
            'SHOES',
            small_black_shoes.transform_name_for_sku()
        )

        medium_pink_tank_top = Product('tank top', 'M', 'pink') 
        self.assertEqual( 
            'TANKTOP', 
            medium_pink_tank_top.transform_name_for_sku()
        ) 
