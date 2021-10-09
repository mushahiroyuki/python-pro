# ch03/06functional/imperative-python.py
squares = [x * x for x in [1, 2, 3, 4, 5]]
for i in squares:
    print(i, end=" ")  # 1 4 9 16 25 
print() # 改行

should = all([True, True, False])
print(should)  # False
should = all([True, True, True])
print(should)  # True

evens = [x for x in [1, 2, 3, 4, 5] if x % 2 == 0]
for i in evens:
    print(i, end=" ")  # 2 4
print()  # 改行
