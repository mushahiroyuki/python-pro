# 複数個の1重のループ
names = ['小山', '中山', '大山', '高山']
for name in names:
    print(f'私は{name}です。')

message = '本日のゲスト： '
for name in names:
    message += f'{name}さん '
print(message)
