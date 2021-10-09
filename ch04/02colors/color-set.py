#@@range_begin(list1)  # ←この行は無視してください
# 集合（set）を使って色を記録
all_colors = set()

with open('all-favorite-colors.txt') as favorite_colors_file:
    for line in favorite_colors_file:  # <1>
        all_colors.add(line.strip())  # <2>

print('琥珀' in all_colors)  # <3>
#@@range_end(list1)  # ←この行は無視してください
print('青' in all_colors)

