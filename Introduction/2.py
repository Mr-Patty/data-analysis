import functools
n = int(input())
a = [i for i in input().split()]
a = sorted(a, key = lambda num: (functools.reduce(lambda a,b: int(a) + int(b), num, 0), int(num)))
for i in a: print(i, end=" ")