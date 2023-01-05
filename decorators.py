# Basic concept of func
# def f1():
#     print("Called f1")
#
# def f2(f):
#     f()
#
# f2(f1)

# Decorated func
# def f1(func):
#     def wrapper():
#         print("Started")
#         func()
#         print("Ended")
#     return wrapper
# @f1
# def f():
#     print("Hello")
#
# # x = f1(f)
# # x()
# f()

# Examples with arguments
# def f1(func):
#     def wrapper(*args, **kwargs):
#         print("Started")
#         func(*args, **kwargs)
#         print("Ended")
#     return wrapper
# @f1
# def f(a, b=8):
#     print(a, b)
#
# f('H1!')

# Second example
def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        val = func(*args, **kwargs)   #  value
        print("Ended")
        return val   # return value
    return wrapper
@f1
def f(a, b=8):
    print(a, b)
f("Hi!")
@f1
def add(x, y):
    return x + y

print(add(4, 5))