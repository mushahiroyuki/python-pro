# 1重のループ、複数ステップ
names = ['小山', '中山', '大山', '高山']
for index, name in enumerate(names):
    greeting = 'こんにちは。私の名前は'
    print(f'{index+1}. {greeting}{name}です。')
