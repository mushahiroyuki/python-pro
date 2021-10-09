#@@range_begin(list1)  # ←この行は無視してください
# 1重のループ、1ステップ
names = ['小山', '中山', '大山', '高山']
for name in names:
    print(name)
#@@range_end(list1)  # ←この行は無視してください


#@@range_begin(list2)  # ←この行は無視してください
# 1重のループ、複数ステップ
names = ['小山', '中山', '大山', '高山']
for index, name in enumerate(names):
    greeting = 'こんにちは。私の名前は'
    print(f'{index+1}. {greeting}{name}です。')

# 結果
# 1. こんにちは。私の名前は小山です。
# 2. こんにちは。私の名前は中山です。
# ...
#@@range_end(list2)  # ←この行は無視してください

#@@range_begin(list3)  # ←この行は無視してください
names = ['小山', '中山', '大山', '高山']
for name in names:
    print(f'私は{name}です。')

message = '本日のゲスト： '
for name in names:
    message += f'{name}さん '
print(message)
#@@range_end(list3)  # ←この行は無視してください

#@@range_begin(list4)  # ←この行は無視してください
# 入れ子になったforループ
def has_duplicates(sequence):
    for index1, item1 in enumerate(sequence):  # <1>
        for index2, item2 in enumerate(sequence):  # <2>
            if item1 == item2 and index1 != index2:  # <3>
                return True
    return False
#@@range_end(list4)  # ←この行は無視してください    
sequence = [0, 5, 10, 7, 19, 4]
print(has_duplicates(sequence))
sequence = [0, 5, 4, 10, 7, 19, 4]
print(has_duplicates(sequence))

