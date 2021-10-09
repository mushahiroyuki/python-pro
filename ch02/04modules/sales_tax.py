#@@range_begin(list1)  # ←この行は無視してください。書籍の本文に引用するためのものです。
# ch02/04modules/sales_tax.py

TAX_RATES_BY_STATE = { # 州ごとの税率
    'MI': 1.06,  # ミシガン州
    # ...
#@@range_end(list1)  # ←この行は無視してください。書籍の本文に引用するためのものです。
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
    tax_rate = TAX_RATES_BY_STATE[state]    
    return total * tax_rate
#@@range_end(list2)  # ←この行は無視してください。書籍の本文に引用するためのものです。

def add_state_tax(total):
    return total * 1.1

def add_city_tax(total):
    return total * 1.1

def add_local_millage_tax(total):
    return total * 1.1




