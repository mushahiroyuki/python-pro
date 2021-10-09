import json
#@@range_begin(list1)
import random

FOODS = [  # <1>
    'ピザ',
    'ハンバーガー',
    'サラダ',
    'スープ',
]


def random_food(request):  # <2>
    return random.choice(FOODS)  # <3>
#@@range_end(list1)


print(random_food(None))
