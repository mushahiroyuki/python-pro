#@@range_begin(list1)
from functools import partial

def pow(x, power=1):
    return x ** power

square = partial(pow, power=2)  # <1>
cube = partial(pow, power=3)  # <2>
#@@range_end(list1)

print(square(3))
print(cube(3))
print(square(8))
print(cube(8))
