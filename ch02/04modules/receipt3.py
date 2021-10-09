#@@range_begin(list1)  # ←この行は無視してください。書籍の本文に引用するためのものです。
import sales_tax

def print_receipt():
    total = 1000.0
    state = 'MI'
    grand_total = sales_tax.add_local_millage_tax(sales_tax.add_city_tax(
        sales_tax.add_state_tax(sales_tax.add_sales_tax(total, state))))
    print(f'合計: {grand_total}')
#@@range_end(list1)  # ←この行は無視してください。書籍の本文に引用するためのものです。

print_receipt()
