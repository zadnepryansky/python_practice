# List Comprehension
greening = 'hello!'
# letter_list = []
# for letter in greening:
#     letter_list.append(letter)
# print(letter_list)

# letter_list = [letter for letter in greening]
# print(letter_list)
#
# number_list = [number for number in '123456789']
# print(number_list)
#
# number_list_1 = [num for num in range(0, 10)]
# print(number_list_1)
# number_list_2 = [num ** 2 for num in range(0, 10)]
# print(number_list_2)
# number_list_3 = [- ((num - 3) / 2) ** 2for num in range(0, 10)]
# print(number_list_3)

number_list = [6, 43, -2, 11, -55, -12, 3, 345, 0]
new_list = [number ** 3 / 2 for number in number_list if number > 0]
print(new_list)
new_list_1 = ['+' if number > 0 else '-' if number < 0 else 'zero' for number in number_list]
print(new_list_1)
