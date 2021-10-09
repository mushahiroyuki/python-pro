# 名前のリスト部分を別関数に
def join_names(names):  # 名前を合体（join）してひとつの文字列にする
    name_string = ''
    for index, name in enumerate(names):
        if index > 0:
            name_string += 'に'
        if index == len(names) -1:
            name_string += '、それから'
        name_string += name
    return name_string

def introduce(title, names):
    print(f'{title}: {join_names(names)}')

introduce('三ばか大将', ['モー', 'ラリー', 'シェンプ'])
introduce('三ばか大将', ['ラリー', 'カーリー', 'モー'])
introduce('忍者タートルズ',  ['ドナテロ', 'ファエロ', 'ミケランジェロ', 'レオナルド'])
introduce('アルビンとチップマンクス', ['アルビン', 'サイモン', 'セオドア'])
introduce('桃太郎', ['イヌ', 'サル', 'キジ'])
