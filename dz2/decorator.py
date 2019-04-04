import time
import random
from functools import wraps

def timeout(rps):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **argv):
            start = time.time()
            result = func(*args, **argv)
            end = time.time() - start
            if (end < 1 / rps):
                time.sleep(1 / rps - end)
            return result
        return wrapper
    return decorator


@timeout(rps=5)
def func():
    pass

if __name__ == "__main__":
    t_start = time.time()
    # print(random.random())
    for i in range(10):
        func()
    t_delta = time.time() - t_start
    print("{:.2f}".format(t_delta))
