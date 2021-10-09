# ch03/06functional/functional-python.py
squares = map(lambda x: x * x, [1, 2, 3, 4, 5])  # 2乗
for i in squares:
    print(i, end=" ")  # 1 4 9 16 25 
print() # 改行

from functools import reduce
should = reduce(lambda x, y: x and y, [True, True, False])
print(should)  # False
should = reduce(lambda x, y: x and y, [True, True, True])
print(should)  # True

evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
for i in evens:
    print(i, end=" ")  # 2 4
print() # 改行
