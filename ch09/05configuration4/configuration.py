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

    formats = {  # <1>
        'application/json': json.dumps({'food': food}),
        'application/xml': f'<response><food>{food}</food></response>',
    }

    return formats.get(request.headers.get('Accept'), food)  # <2>
#@@range_end(list1)
