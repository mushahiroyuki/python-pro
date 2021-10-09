from product import Product

class TestProduct: 
    def test_transform_name_for_sku(self): 
        small_black_shoes = Product('shoes', 'S', 'black') 
        assert small_black_shoes.transform_name_for_sku() == 'SHOES' 

    def test_transform_color_for_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        assert small_black_shoes.transform_color_for_sku() == 'BLACK'

    def test_generate_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        assert small_black_shoes.generate_sku() == 'SHOES-S-BLACK'
