#@@range_begin(list1)
# メモリにすべて読み込んでから処理
color_counts = {}
with open('all-favorite-colors.txt') as favorite_colors_file:
    favorite_colors = favorite_colors_file.read().splitlines()  # <1>

for color in favorite_colors:
    if color in color_counts:
        color_counts[color] += 1
    else:
        color_counts[color] = 1
#@@range_end(list1)
print(color_counts)
