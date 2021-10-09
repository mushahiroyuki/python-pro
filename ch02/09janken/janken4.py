# 属性にアクセスするのにselfを用いる
import random
OPTIONS = ['グー', 'チョキ', 'パー']

class JankenSimulator:
    def __init__(self):
        self.computer_choice = None
        self.human_choice = None

    def get_computer_choice(self):  # <1>
        self.computer_choice = random.choice(OPTIONS)

    def get_human_choice(self):
        choice_number = int(input('「グー」か「チョキ」か「パー」を番号で選んでください: '))
        self.human_choice = OPTIONS[choice_number - 1]

    def print_options(self):
        print('\n'.join(f'({i}) {option.title()}' for i, option in enumerate(OPTIONS, 1)))

    def print_choices(self):  # <2>
        print(f'あなたが選んだのは「{self.human_choice}」です。')  # <3>
        print(f'コンピュータが選んだのは「{self.computer_choice}」です。')

    def print_win_lose(self, human_beats, human_loses_to):
        if self.computer_choice == human_loses_to:
            print(f'残念でした。{self.computer_choice}の勝ちです。')
        elif self.computer_choice == human_beats:
            print(f'おめでとうございます！ {self.human_choice}の勝ちです。')

    def print_result(self):
        if self.human_choice == self.computer_choice:
            print('引き分けです。')

        if self.human_choice == 'グー':
            self.print_win_lose('チョキ', 'パー')
        elif self.human_choice == 'パー':
            self.print_win_lose('グー', 'チョキ')
        elif self.human_choice == 'チョキ':
            self.print_win_lose('パー', 'グー')

    def simulate(self):
        self.print_options()
        self.get_human_choice()
        self.get_computer_choice()
        self.print_choices()
        self.print_result()

#@@range_begin(list3)  # ←この行は無視してください。書籍の本文に引用するためのものです。
janken = JankenSimulator()
janken.simulate()
#@@range_end(list3)  # ←この行は無視してください。書籍の本文に引用するためのものです。
