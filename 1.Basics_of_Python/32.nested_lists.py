# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12, 13]]
# print(nested_list)
# print(len(nested_list))
# print(len(nested_list[1]))
# print(len(nested_list[-1]))
# print(nested_list[1][2])
#
# # Get number 12
# print(nested_list[3][2])
# print(nested_list[-1][2])
# print(nested_list[3][-2])
# print(nested_list[-1][-2])

# Print nested list
nested_list = [[1, 2, 3], [4, 5, 6, True], [7, 8, 9, 'text'], [10, 11, 12, 13], [False, 23, 'hello']]

# for inner_list in nested_list:
#     print(inner_list)
#
# for inner_list in nested_list:
#     for number in inner_list:
#         print(number)

[[print(number) for number in inner_list] for inner_list in nested_list]