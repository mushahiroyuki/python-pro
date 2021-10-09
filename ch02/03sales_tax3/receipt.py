from sales_tax import add_sales_tax

def print_receipt():
    total = 1000.0
    state = 'MI'
    print(f'合計: {total}')
    print(f'税込合計: {add_sales_tax(total, state)}')


print_receipt()
