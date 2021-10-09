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
    food = random.choice(FOODS)

    if request.headers.get('Accept') == 'application/json':
        return json.dumps({'food': food})
    elif request.headers.get('Accept') == 'application/xml':  # <1>
        return f'<response><food>{food}</food></response>'
    else:
        return food
#@@range_end(list1)
