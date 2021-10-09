# 単純に繰り返す
names = ['モー', 'ラリー', 'シェンプ']
message = '三ばか大将：'
for index, name in enumerate(names):
    if index > 0:
        message += 'に'
    if index == len(names) - 1:
        message += '、それから'
    message += name
print(message)

names = ['ラリー', 'カーリー', 'モー']
message = '三ばか大将：'
for index, name in enumerate(names):
    if index > 0:
        message += 'に'
    if index == len(names) -1:
        message += '、それから'
    message += name
print(message)
