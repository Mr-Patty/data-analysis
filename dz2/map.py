import re
from operator import setitem
from functools import reduce

def solution1(arg):
    return list(map(
        lambda x: int(''.join(re.findall(r'\d+', x))[::-1]),
        arg
    ))

def solution2(arg):
    return list(map(
        lambda x: x[0] * x[1],
        arg
    ))

def solution3(arg):
    return list(filter(
        lambda x: x % 6 == 0 or x % 6 == 2 or x % 6 == 5,
        arg
    ))

def solution4(arg):
    return list(filter(
        lambda x: x,
        arg
    ))

def solution5(arg):
    return list(map(
        lambda x: setitem(x, "square", x["width"] * x["length"]),
        arg
    ))

def solution6(arg):
    return list(map(
        lambda x: dict(zip(list(x.keys()) + ["square"],
            list(x.values()) + [x["width"] * x["length"]])),
        arg
    ))

def solution7(arg):
    return reduce(lambda x, y: x.intersection(y), arg)

def solution8(arg):
    return reduce(
        lambda x, y:
            (y in x and setitem(x, y, x[y] + 1)) or
            (not y in x and setitem(x, y, 1)) or
            x,
        arg,
        dict()
    )

def solution9(arg):
    return list(map(
        lambda x: x['name'],
        list(filter(lambda x: x['gpa'] > 4.5, arg))
    ))

def solution10(arg):
    return list(filter(
        lambda x:
            sum(map(lambda x: int(x), x[0::2])) ==
            sum(map(lambda x: int(x), x[1::2])),
        arg
    ))

solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}

rooms = [
    {"name": "комната1", "width": 2, "length": 4},
    {"name": "комната2", "width": 2.5, "length": 5.6},
    {"name": "кухня", "width": 3.5, "length": 4},
    {"name": "туалет", "width": 1.5, "length": 1.5},
]

students = [
    {'name': 'Alina', 'gpa': 4.57},
    {'name': 'Sergey', 'gpa': 5.0},
    {'name': 'Nastya', 'gpa': 4.21},
    {'name': 'Valya', 'gpa': 4.72},
    {'name': 'Anton', 'gpa': 4.32},
]

if __name__ == "__main__":
    print(solution1(['12', '25.6', '84,02', '  69-91']))
    print(solution2(zip(range(2, 5), range(3, 9, 2))))
    print(solution3(range(20)))
    print(solution4(['', 25, None, 'python', 0.0, [], ('msu', '1755-01-25')]))
    import copy
    rooms1 = copy.deepcopy(rooms)
    solution5(rooms)
    print(rooms)
    print(solution6(rooms1))
    print(rooms1)
    print(solution7([{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}, {3, 4, 5, 6, 7}]))
    print(solution8([1, 2, 1, 1, 3, 2, 3, 2, 4, 2, 4]))
    print(solution9(students))
    print(solution10(['165033', '477329', '631811', '478117', '475145', '238018', '917764', '394286']))
