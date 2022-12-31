# greetings = ['hello', 'hi', 'hey', 'hola']
# new_list = []
# for letter in greetings:
#     new_list.append(letter[1])
# print(new_list)

# new_list_1 = [letter[1] for letter in greetings]
# print(new_list_1)

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_number = []
# for number in digits:
#     if number % 2 == 1:
#         new_number.append(number)
# print(new_number)

new_number_1 = [number for number in digits if number % 2 == 1]
print(new_number_1)

