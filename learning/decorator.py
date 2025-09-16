import time


def log(func):
    def wrap(*args):
        result = func(*args)
        print(f"Sum is {result}")
        return result
    return wrap


def timer(func):
    def wrap(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Function took {end-start:.4f} seconds")
        return result
    return wrap


@log
@timer
def sum(n1, n2, n3):
    return n1 + n2 + n3


sum(1, 2, 3)
