def product(arg):
    if arg == []:
        yield ()
    else:
        for i in arg[0]:
            for j in product(arg[1:]):
                yield (i,) + j

if __name__ == '__main__':

    a = [[0, 1], 'python']
    for e in product(a):
        print(e)
