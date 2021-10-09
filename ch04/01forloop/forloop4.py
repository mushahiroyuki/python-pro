#@@range_begin(list1)
# 入れ子になったforループ
def has_duplicates(sequence):
    for index1, item1 in enumerate(sequence):  # <1>
        for index2, item2 in enumerate(sequence):  # <2>
            if item1 == item2 and index1 != index2:  # <3>
                return True
    return False
#@@range_end(list1)
sequence = [0, 5, 10, 7, 19, 4]
print(has_duplicates(sequence))
sequence = [0, 5, 4, 10, 7, 19, 4]
print(has_duplicates(sequence))

