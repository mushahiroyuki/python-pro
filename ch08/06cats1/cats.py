class BigCat:   # 大型猫科動物
    def eats(self):   # 食べる
        return ['齧歯動物']


class Lion(BigCat):  # <1>
    def eats(self):
        return ['ヌー']


class Tiger(BigCat):  # <2>
    def eats(self):
        return ['水牛']


class Liger(Lion, Tiger):  # <3>
    def eats(self):
        return super().eats() + ['兎', '牛', '豚', '鶏']


if __name__ == '__main__':
    lion = Lion()
    print('ライオンが食べるもの：', lion.eats())
    tiger = Tiger()
    print('トラが食べるもの：', tiger.eats())
    liger = Liger()
    print('ライガーが食べるもの：', liger.eats())
