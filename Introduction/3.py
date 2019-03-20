n, k = map(lambda x: int(x), input().split())
c = n - k + 2
h = (c // 2) * [1, 2]
if c % 2 == 1: h.append(1)
for i in range(3, k + 1):
    h.append(i)
for i in h:
    print(i, end = " ")