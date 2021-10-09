# ch05/09tryitout2/cart.py
from collections import defaultdict

class ShoppingCart:
    def __init__(self):
        self.products = defaultdict(lambda: defaultdict(int)) 

    def add_product(self, product, quantity=1):
        self.products[product.generate_sku()]['quantity'] += quantity

    def remove_product(self, product, quantity=1):
        sku = product.generate_sku()
        self.products[sku]['quantity'] -= quantity
#@@range_begin(list1)  # ←この行は無視してください        
        if self.products[sku]['quantity'] <= 0:
            del self.products[sku]
#@@range_end(list1)  # ←この行は無視してください
