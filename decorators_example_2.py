# Python Decorators - Example 2
import time

def timer(func):
    def wrapper():
        before = time.time()
        func()
        print(f"Function took: {time.time() - before}, seconds")
    return wrapper()

@timer
def run():
    time.sleep(2)

run()