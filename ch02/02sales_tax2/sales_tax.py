#@@range_begin(list1)
TAX_RATES_BY_STATE = { # 州ごとの売上税率
    'MI': 1.06,  # ミシガン州
    # ...
#@@range_end(list1)
    'AK': 1.00,  # アラスカ州
    'AL': 1.04,  # アラバマ州
    'AR': 1.065, # アーカンソー州
    'AZ': 1.056, # アリゾナ州
    # ...
    # ...
    # ...
    'WY': 1.04   # ワイオミング州
#@@range_begin(list2)  # ←この行は無視してください。書籍の本文に引用するためのものです。
}

def add_sales_tax(total, state):
    return total * TAX_RATES_BY_STATE[state]
#@@range_end(list2)  # ←この行は無視してください。書籍の本文に引用するためのものです。

def test():
    total = 1000
    grand_total = add_sales_tax(total, 'MI')
    print(f"合計金額={grand_total}")

if __name__ == '__main__': test()  # ほかのプログラムにimportされた場合は実行しない


    
