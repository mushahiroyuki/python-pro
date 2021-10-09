class Teller:  # 窓口係
    def deposit(self, amount, account):  # 預け入れ
        account.deposit(amount)


class CorruptTeller(Teller):  # <1>  # 邪悪な窓口係
    def __init__(self):
        self.coffers = 0  # 金庫

    def deposit(self, amount, account):  # <2>
        self.coffers += amount * 0.01  # <3>  # 少し自分の金庫に入れる
        super().deposit(amount * 0.99, account)  # <4>
