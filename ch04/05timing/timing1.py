#@@range_begin(list1)
from timeit import timeit

setup = 'from datetime import datetime'  # <1>
statement = 'datetime.now()'  # <2>
result = timeit(setup=setup, stmt=statement, number=1000)  # <3>
print(f'実行時間の平均： {result / 1000}s == {result}ms')
#@@range_end(list1)
