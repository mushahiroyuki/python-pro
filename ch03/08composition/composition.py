#@@range_begin(list1)
# ミックスイン
class SpeakMixin:  # <1>
    def speak(self):
        name = self.__class__.__name__.lower()
        print(f'一匹の{name}が「こんにちは！」と言った。')

class RollOverMixin:  # <2>
    def roll_over(self):
        print('横回転をした！')

class Dog(SpeakMixin, RollOverMixin):  # <3>
    pass  # 何もしない
#@@range_end(list1)

# Dogクラスを利用
#@@range_begin(list2)
dog = Dog()
dog.speak()
dog.roll_over()
#@@range_end(list2)
