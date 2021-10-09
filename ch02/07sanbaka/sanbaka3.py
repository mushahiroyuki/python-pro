# 関数にまとめる
def introduce_stooges(names): # 三ばか大将を紹介
    message = '三ばか大将：'
    
    for index, name in enumerate(names):
        if index > 0:
            message += 'に'
        if index == len(names) - 1:
            message += '、それから'
        message += name
    print(message)

introduce_stooges(['モー', 'ラリー', 'シェンプ'])
introduce_stooges(['ラリー', 'カーリー', 'モー'])
