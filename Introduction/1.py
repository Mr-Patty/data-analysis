n, b = int(input()), []
for s in input().split():
    if not int(s) in b: b.append(int(s)), print(int(s), end=" ")
print()
print(n - len(b))
