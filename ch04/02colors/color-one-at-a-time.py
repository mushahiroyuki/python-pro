#@@range_begin(list1)
# 1行ずつ読み込み
color_counts = {}
with open('all-favorite-colors.txt') as favorite_colors_file:
    for color in favorite_colors_file:  # <1>
        color = color.strip()  # <2>

        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1
#@@range_end(list1)
print(color_counts);
