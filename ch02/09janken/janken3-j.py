# 日本語識別子版
# 属性にアクセスするのにselfを用いる
import random

手の選択肢 = ['グー', 'チョキ', 'パー']  # Rock, Scissors, Paper


class ジャンケンシミュレータ:
    def __init__(self):
        self.コンピュータの選択肢 = None
        self.ユーザーの選択肢 = None

    def get_コンピュータの選択肢(self):  # <1>
        self.コンピュータの選択肢 = random.choice(手の選択肢)

    def get_ユーザーの選択肢(self):
        選択肢の番号 = int(input('「グー」か「チョキ」か「パー」を番号で選んでください: '))
        self.ユーザーの選択肢 = 手の選択肢[選択肢の番号 - 1]

    def print_手の選択肢(self):
        print('\n'.join(f'({i}) {ひとつの手.title()}' for i, ひとつの手 in enumerate(手の選択肢, 1)))

    def print_それぞれの手(self):  # <2>
        print(f'あなたが選んだのは「{self.ユーザーの選択肢}」です。')  # <3>
        print(f'コンピュータが選んだのは「{self.コンピュータの選択肢}」です。')

    def print_勝敗(self, 人間が勝つ手, 人間が負ける手):
        if self.コンピュータの選択肢 == 人間が負ける手:
            print(f'残念でした。{self.コンピュータの選択肢}の勝ちです。')
        elif self.コンピュータの選択肢 == 人間が勝つ手:
            print(f'おめでとうございます！ {self.ユーザーの選択肢}の勝ちです。')

    def print_結果(self):
        if self.ユーザーの選択肢 == self.コンピュータの選択肢:
            print('引き分けです。')

        if self.ユーザーの選択肢 == 'グー':
            self.print_勝敗('チョキ', 'パー')
        elif self.ユーザーの選択肢 == 'パー':
            self.print_勝敗('グー', 'チョキ')
        elif self.ユーザーの選択肢 == 'チョキ':
            self.print_勝敗('パー', 'グー')

    def シミュレートする(self):
        self.print_手の選択肢()
        self.get_ユーザーの選択肢()
        self.get_コンピュータの選択肢()
        self.print_それぞれの手()
        self.print_結果()

# 実行
ジャンケンマシン = ジャンケンシミュレータ()
ジャンケンマシン.シミュレートする()
