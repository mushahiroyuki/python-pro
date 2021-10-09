#@@range_begin(list1)
NAMES = ['小山', '大山', '中山']

def print_greetings():  # <1>
    greeting_pattern = '{name}さんに、ごあいさつ。'
    nice_person_pattern = '{name}さんはとても良い人です！'
    for name in NAMES:
        print(greeting_pattern.format(name=name))
        print(nice_person_pattern.format(name=name))
#@@range_end(list1)

if __name__ == '__main__':   # ほかのプログラムにimportされた場合は実行しない
    print_greetings()
