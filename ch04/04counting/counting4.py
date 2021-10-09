#@@range_begin(list1)
# 第4版 ラムダ関数の利用
from collections import Counter

def get_number_with_highest_count(counts): # countsの要素のうち、頻度最高のものを得る
    return max(  # <1>
        counts,
        key=lambda number: counts[number] 
        # 第2引数keyの値として「numberを引数として受け取りcount[number]を返す関数」を指定
    )

def most_frequent(numbers):
    counts = Counter(numbers)
    return get_number_with_highest_count(counts)
#@@range_end(list1)

print (most_frequent([0, 3, 5, 10, 20, 5, 3, 4, 20, 4, 5, 3, 12, 4]))
