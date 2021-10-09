#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
def get_united_states_capitals():
    us_capitals_by_state = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
        'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford',
        'Delaware': 'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Idaho': 'Boise',
        'Illinois': 'Springfield',
        'Indiana': 'Indianapolis',
        'Iowa': 'Des Moines',
        'Kansas': 'Topeka',
        'Kentucky': 'Frankfort',
        'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta',
        'Maryland': 'Annapolis',
        'Massachusetts': 'Boston',
        'Michigan': 'Lansing',
        'Minnesota': 'St. Paul',
        'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City',
        'Montana': 'Helen',
        'Nebraska': 'Lincol',
        'Nevada': 'Carson Cit',
        'New Hampshire': 'Concor',
        'New Jersey': 'Trento',
        'New Mexico': 'Santa F',
        'New York': 'Alban',
        'North Carolina': 'Raleig',
        'North Dakota': 'Bismarc',
        'Ohio': 'Columbu',
        'Oklahoma': 'Oklahoma Cit',
        'Oregon': 'Sale',
        'Pennsylvania': 'Harrisbur',
        'Rhode Island': 'Providenc',
        'South Carolina': 'Columbi',
        'South Dakota': 'Pierr',
        'Tennessee': 'Nashvill',
        'Texas': 'Austi',
        'Utah': 'Salt Lake Cit',
        'Vermont': 'Montpelie',
        'Virginia': 'Richmon',
        'Washington': 'Olympi',
        'West Virginia': 'Charlesto',
        'Wisconsin': 'Madiso',
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
        'Wyoming': 'Cheyenn',
    }

    capitals = us_capitals_by_state.values()
    return sorted(capitals)
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。

print(get_united_states_capitals())

