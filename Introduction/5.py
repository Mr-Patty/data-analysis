def output(x, y, h):
    *map(lambda i: print("? " + str(i)), list(range(y + h, x + h, h))),

mx, mn = 100000, 0
answer = False
while not answer:
    lst = []
    h = (mx - mn) // 5
    output(mx, mn, h)
    print("+", flush=True)
    for i in range(5):
        x = int(input())
        lst.append(x)
    for i, v in enumerate(lst, 0):
        if v == 1:
            mx = mn + h * (i + 1)
            mn = mn + h * i
            break
        if i == 9:
            mn = mn + h * (i + 1)
            answer = True
    if h == 1:
        answer = True
print("! " + str(mn))
