#@@range_begin(list1)
from datetime import datetime
import locale  # 日時等日本語化のため
locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')  # 日本語に設定

class Greeter:
    def __init__(self, name):
        self.name = name

    def _day(self):  # <1>       
        return datetime.now().strftime('%A')

    def _part_of_day(self):  # <2>
        current_hour = datetime.now().hour

        if current_hour < 12:
            part_of_day = '午前'
        elif 12 <= current_hour < 17:  # 「elif current_hour < 17:」でも同じ
            part_of_day = '午後'
        else:
            part_of_day = '夜'

        return part_of_day

    def greet(self, store):  # <3>
        print(f'{store}へようこそ！ 私、{self.name}と申します。')
        print(f'{self._day()}の{self._part_of_day()}、いかがお過ごしですか？')
        print('本日のお客様に20% OFFのクーポンを差し上げます！')
#@@range_end(list1)

if __name__ == '__main__':   # ほかのプログラムにimportされた場合は実行しない
    greeter = Greeter("竈門");
    greeter.greet("Pythonプロショップ")
