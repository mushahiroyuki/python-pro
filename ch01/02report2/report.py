col1_name = col2_name = col3_name = col4_name = "ABC"
first_val = second_val = third_val =  fourth_val = "99"

#@@range_begin(list1)
DELIMITER = '\t'
print(DELIMITER.join([col1_name, col2_name, col3_name, col4_name]))
print(DELIMITER.join([first_val, second_val, third_val, fourth_val]))
#@@range_end(list1)

