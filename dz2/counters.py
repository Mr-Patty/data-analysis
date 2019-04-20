from functools import wraps

def counter(func):
    @wraps(func)
    def wrapper(*args, **argv):
        if wrapper.count == 0:
            wrapper.ncalls = 0
            wrapper.rdepth = 0
        wrapper.count += 1
        result = func(*args, **argv)
        wrapper.rdepth = max(wrapper.rdepth, wrapper.count)
        wrapper.ncalls += 1
        wrapper.count -= 1
        return result
    wrapper.ncalls = 0
    wrapper.rdepth = 0
    wrapper.count = 0
    return wrapper

if __name__ == "__main__":
    func2(0, 5)
    print(func2.ncalls, func2.rdepth)

    func2(0, 3)
    print(func2.ncalls, func2.rdepth)
