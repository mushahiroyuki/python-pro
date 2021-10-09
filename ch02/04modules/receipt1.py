#@@range_begin(list1)  # ←この行は無視してください。書籍の本文に引用するためのものです。
from sales_tax import add_sales_tax, add_state_tax, add_city_tax, add_local_millage_tax
#@@range_end(list1)  # ←この行は無視してください。書籍の本文に引用するためのものです。

def print_receipt():
    total = 1000.0
    state = 'MI'
    grand_total = add_local_millage_tax(add_city_tax(add_state_tax(add_sales_tax(total, state))))
    print(f'合計: {grand_total}')

print_receipt()


