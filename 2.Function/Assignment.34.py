# def cat_voice():
#     print('Meow!')
#
# def dog_voice():
#
#     print('Woof!')
#
# dog_voice()
# cat_voice()



# def cat_voice():
#     return 'Meow!'
#
# def dog_voice():
#     return 'Woof!'
#
# print(cat_voice())
# print(cat_voice())
# print(dog_voice())
# print(dog_voice())

# def get_voice(voice):
#     return str(voice) + '!'
# print(get_voice('Meow'))

# With List Comprehension
# def get_odd_number_list(a, b):
#     number_list = list(range(a, b + 1))
#     odd_number_list = [number for number in number_list if number % 2 == 1]
#     return odd_number_list


# Without List Comprehension
def get_odd_number_list(a, b):
    number_list = list(range(a, b + 1))
    odd_number_list = []
    for number in number_list:
        if number % 2 == 1:
            odd_number_list.append(number)
    return odd_number_list