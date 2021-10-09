from abc import ABC, abstractmethod


class Predator(ABC):  # <1>
    @abstractmethod  # <2>
    def eat(self, prey):  # <3>
        pass # <4>


class Bear(Predator):  # <5>
    def eat(self, prey):  # <6>
        print(f'熊が{prey}を一撃！')


class Owl(Predator):
    def eat(self, prey):
        print(f'フクロウが{prey}めがけて急降下！')


class Chameleon(Predator):
    def eat(self, prey):
        print(f'カメレオンが舌を伸ばして{prey}をペロリ！')

class Human(Predator):
    def talk(self):
        print(f'人間が話をした')

if __name__ == '__main__':
    bear = Bear()
    bear.eat('シカ')
    owl = Owl()
    owl.eat('ネズミ')
    chameleon = Chameleon()
    chameleon.eat('ハエ')

    human = Human()
    human.talk()
