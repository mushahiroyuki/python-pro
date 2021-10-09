#@@range_begin(list1)
class Tire:  # <1>
    def __repr__(self):
        return 'ゴムのタイヤ'


class Frame:
    def __repr__(self):
        return 'アルミのフレーム'


class Bicycle:
    def __init__(self, front_tire, back_tire, frame):  # <1>
        self.front_tire = front_tire
        self.back_tire = back_tire
        self.frame = frame

    def print_specs(self):
        print(f'フレーム: {self.frame}')
        print(f'前のタイヤ: {self.front_tire}。後ろのタイヤ: {self.back_tire}')


if __name__ == '__main__':
    bike = Bicycle(Tire(), Tire(), Frame())  # <2>
    bike.print_specs()
#@@range_end(list1)
    
