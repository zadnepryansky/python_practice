# Python Decorators - Example 3
import datetime

def log(func):
    def wrapper(*args, **kwargs):
        with open("logs_decorator_example_3.txt", "a") as f:
            f.write("Called function with " + " ".join([str(arg) for arg in args]) + " at " + str(datetime.datetime.now()) + "\n")
        val = func(*args, **kwargs)
        return val

    return wrapper

@log
def run(a, b, c=9):
    print(a + b + c)

run(1, 3, 9)