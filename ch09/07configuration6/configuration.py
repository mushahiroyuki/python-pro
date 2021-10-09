import json
import random

FOODS = [
    'ピザ',
    'ハンバーガー',
    'サラダ',
    'スープ',
]



def to_json(food):  # <1>
    return json.dumps({'food': food})


def to_xml(food):
    return f'<response><food>{food}</food></response>'


#@@range_begin(list1)
def get_format_function(accept=None):  # <1>
    formats = {
        'application/json': to_json,
        'application/xml': to_xml,
    }

    return formats.get(accept, lambda val: val)


def random_food(request):  # <2>
    food = random.choice(FOODS)
    format_function = get_format_function(request.headers.get('Accept'))  # <3>
    return format_function(food)
#@@range_end(list1)
