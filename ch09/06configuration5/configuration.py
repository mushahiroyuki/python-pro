import json
import random

FOODS = [
    'ピザ',
    'ハンバーガー',
    'サラダ',
    'スープ',
]


#@@range_begin(list1)
def to_json(food):  # <1>
    return json.dumps({'food': food})


def to_xml(food):
    return f'<response><food>{food}</food></response>'


def random_food(request):
    food = random.choice(FOODS)

    formats = {  # <2>
        'application/json': to_json,
        'application/xml': to_xml,
    }

    format_function = formats.get(  # <3>
        request.headers.get('Accept'),
        lambda val: val  # <4>
    )
    return format_function(food)  # <5>
#@@range_end(list1)
