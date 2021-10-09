#@@range_begin(list1)  # ←この行は無視してください
# rangeの処理を真似たもの
def range(*args):
    if len(args) == 1: # <1>
        start = 0
        stop = args[0]
    else:
        start = args[0]
        stop = args[1]

    current = start

    while current < stop:
        yield current  # <2>
        current += 1  # <3>
#@@range_end(list1)  # ←この行は無視してください


# Creating a generator for calculating squares of numbers in a list
#@@range_begin(list2)  # ←この行は無視してください
def squares(items):
    for item in items:
        yield item ** 2
#@@range_end(list2)  # ←この行は無視してください

print(list(squares(range(10))))
print(list(squares(range(11,21))))
