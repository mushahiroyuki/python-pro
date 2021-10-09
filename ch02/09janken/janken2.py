# 関数を抽出
import random

OPTIONS = ['グー', 'チョキ', 'パー']

def get_computer_choice():
    return random.choice(OPTIONS)

def get_human_choice():
    choice_number = int(input('「グー」か「チョキ」か「パー」を番号で選んでください: '))
    return OPTIONS[choice_number - 1]

def print_options():
    print('\n'.join(f'({i}) {option.title()}' for i, option in enumerate(OPTIONS, 1)))

def print_choices(human_choice, computer_choice):
    print(f'あなたが選んだのは「{human_choice}」です。')
    print(f'コンピュータが選んだのは「{computer_choice}」です。')

def print_win_lose(human_choice, computer_choice, human_beats, human_loses_to):
    if computer_choice == human_loses_to:
        print(f'残念でした。「{computer_choice}」の勝ちです。')
    elif computer_choice == human_beats:
        print(f'おめでとうございます！ 「{human_choice}」の勝ちです。')

def print_result(human_choice, computer_choice):
    if human_choice == computer_choice:
        print('引き分けです。')

    if human_choice == 'グー':
        print_win_lose('グー', computer_choice, 'チョキ', 'パー')
    elif human_choice == 'パー':
        print_win_lose('パー', computer_choice, 'グー', 'チョキ')
    elif human_choice == 'チョキ':
        print_win_lose('チョキ', computer_choice, 'パー', 'グー')

print_options()  # 選択肢を表示
human_choice = get_human_choice()  # 人間が選択したもの
computer_choice = get_computer_choice() # コンピュータが選択したもの
print_choices(human_choice, computer_choice) # 選択したものを印刷
print_result(human_choice, computer_choice)  # 結果を印刷
