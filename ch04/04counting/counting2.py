#@@range_begin(list1)
# 第2版 defaultdictの利用
from collections import defaultdict  # <1>

def get_number_with_highest_count(counts):
    max_count = 0
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            number_with_highest_count = number
    return number_with_highest_count

def most_frequent(numbers):
    counts = defaultdict(int)  # <2>
    for number in numbers:
        counts[number] += 1  # <3>

    return get_number_with_highest_count(counts)
#@@range_end(list1)

print (most_frequent([0, 3, 5, 10, 20, 5, 3, 4, 20, 4, 5, 3, 12, 4]))

