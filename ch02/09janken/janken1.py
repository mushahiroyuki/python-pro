# 最初のコード
import random

options = ['グー', 'チョキ', 'パー']  # 選択肢
print('(1) グー\n(2) チョキ\n(3) パー')
human_choice = options[int(input('「グー」か「チョキ」か「パー」を番号で選んでください: ')) - 1]
print(f'あなたが選んだのは「{human_choice}」です。')
computer_choice = random.choice(options)  # コンピュータが選択したもの
print(f'コンピュータが選んだのは「{computer_choice}」です。')
if human_choice == 'グー':   # 人間が選択したものが「グー」ならば
    if computer_choice == 'パー':
        print('残念でした。パーの勝ちです。')
    elif computer_choice == 'チョキ':
        print('おめでとうございます！ グーの勝ちです。')
    else:
        print('引き分けです。')
elif human_choice == 'パー':
    if computer_choice == 'チョキ':
        print('残念でした。チョキの勝ちです。')
    elif computer_choice == 'グー':
        print('おめでとうございます！ パーの勝ちです。')
    else:
        print('引き分けです。')
elif human_choice == 'チョキ':
    if computer_choice == 'グー':
        print('残念でした。グーの勝ちです。')
    elif computer_choice == 'パー':
        print('おめでとうございます！ チョキの勝ちです。')
    else:
        print('引き分けです！')
