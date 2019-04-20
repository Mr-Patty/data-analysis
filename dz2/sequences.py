def generate(n, open, close, ans):
    if open + close == 2 * n:
        yield ans
    if open < n:
        yield from generate(n, open + 1, close, ans + '(')
    if open > close:
        yield from generate(n, open, close + 1, ans + ')')

def brackets(n):
    yield from generate(n, 0, 0, "")

if __name__ == "__main__":
    n = int(input())
    for i in brackets(n):
        print(i)
