# ほかのグループにも対応
def introduce(title, names):  # 紹介する。グループ名と名前のリストが引数
    message = f'{title}: '
    for index, name in enumerate(names):
        if index > 0:
            message += 'に'
        if index == len(names) - 1:
            message += '、それから'
        message += name
    print(message)

introduce('三ばか大将', ['モー', 'ラリー', 'シェンプ'])
introduce('三ばか大将', ['ラリー', 'カーリー', 'モー'])
introduce('忍者タートルズ',  ['ドナテロ', 'ファエロ', 'ミケランジェロ', 'レオナルド'])
introduce('アルビンとチップマンクス', ['アルビン', 'サイモン', 'セオドア'])
