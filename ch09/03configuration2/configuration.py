import json
import random

FOODS = [
    'ピザ',
    'ハンバーガー',
    'サラダ',
    'スープ',
]

#@@range_begin(list1)
def random_food(request):
    food = random.choice(FOODS)  # <1>

    if request.headers.get('Accept') == 'application/json':  # <2>
        return json.dumps({'food': food})
    else:
        return food  # <3>
#@@range_end(list1)
