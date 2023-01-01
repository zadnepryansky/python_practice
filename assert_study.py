def check_assert(num):
    assert type(num) == int, 'this is not int'
    return num ** 2


print(check_assert('d'))