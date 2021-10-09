import random

def sort_expensive():
    the_list = random.sample(range(1_000_000), 1000) # 「_」は桁区切り
    the_list.sort()

def sort_cheap():
    the_list = random.sample(range(1_000), 10)
    the_list.sort()

if __name__ == '__main__':
    sort_expensive()
    for i in range(1000):
        sort_cheap()
