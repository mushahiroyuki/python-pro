#@@range_begin(list1)
class Bird:
    def fly(self):
        print('飛行中！')
#@@range_end(list1)

#@@range_begin(list2)
class Hummingbird(Bird):
    def fly(self):
        print('高速に羽ばたき中！')
#@@range_end(list2)

#@@range_begin(list3)
class Penguin(Bird):
    def fly(self):
        print('飛べません！')
#@@range_end(list3)

a = Bird();
a.fly()
b = Hummingbird();
b.fly()
c = Penguin();
c.fly()
