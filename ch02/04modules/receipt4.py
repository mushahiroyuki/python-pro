#@@range_begin(list1)  # ←この行は無視してください。書籍の本文に引用するためのものです。
# ch02/04modules/receipt4.py
from sales_tax import *

def print_receipt():
    total = 1000.0
    state = 'MI'
    # 「sales_tax.」は不要になるが、
    grand_total = add_local_millage_tax(add_city_tax(   
        add_state_tax(add_sales_tax(total, state))))
    print(f'合計: {grand_total}')
#@@range_end(list1)  # ←この行は無視してください。書籍の本文に引用するためのものです。

print_receipt()
