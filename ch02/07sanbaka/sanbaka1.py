# 最初のバージョン
names = ['ラリー', 'カーリー', 'モー']
message = '三ばか大将：'
for index, name in enumerate(names): # namesの各要素をループ
    if index > 0:
        message += 'に'
    if index == len(names) - 1:
        message += '、それから'
    message += name
print(message)
