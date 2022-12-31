from functools import wraps


def print_args(function):
    def wrapper(*args, **kwargs):
        print('args: ', args)
        print('kwargs: ', kwargs)
        return function(*args, **kwargs)
    return wrapper


@print_args
def some_func():
    print('Some code')


some_func()
