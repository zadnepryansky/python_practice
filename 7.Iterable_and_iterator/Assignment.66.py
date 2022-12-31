def get_infinite_square_generator():
    number = 1
    while True:
        yield number * number
        number += 1


infinite_square_generator = get_infinite_square_generator()
print(next(infinite_square_generator))
print(next(infinite_square_generator))
