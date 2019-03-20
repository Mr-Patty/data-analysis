# Я знаю, решение не эффективное и так вообще скорее всего делать нехорошо, но мне было просто интересно будет ли это работать :)
# Основной код, не считая обьявления класса, получился более лаконичным и коротким, а вот определять один хеш для всего класса кажется не очень правильно.
# Мне пришлось на это пойти, потому что в питоне множетства реализованы через хеш-таблицы, а не через деревья, как в других языках.
def inter(a, b):
    return min(a.y, b.y) - max(a.x, b.x)

class Point:  
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return str((self.x, self.y))
    def __repr__(self):
        return str((self.x, self.y))
    def __eq__(self, other):
        return inter(self, other) >= 0
    def __hash__(self):
        return hash(1)

n, k = int(input()), int(input())
check = set()
for i in range(k):
    x, y = map(lambda x: int(x), input().split())
    p = Point(x, y)
    while p in check:
        check.remove(p)
    check.add(p)

print(len(check))