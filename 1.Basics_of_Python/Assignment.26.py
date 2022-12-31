even_numbers_sum = 0

for number in range(10, 31):
    if number % 2 == 0:
        even_numbers_sum += number

print(even_numbers_sum)

# number = input('Please, enter any integer number')
#
# for _ in range(int(number)):
#     print('Hello!')