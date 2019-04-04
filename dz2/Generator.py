def solution1(arg):
    return [i * 4 for i in arg]

def solution2(arg):
    return [v * (i + 1) for i, v in enumerate(arg)]

def solution3(arg):
    return [i for i in arg if i % 3 == 0 or i % 5 == 0]

def solution4(arg):
    return [i for j in arg for i in j]

def solution5(arg):
    return [
        (x, y, z)
        for x in range(1, arg + 1)
        for y in range(1, arg + 1) if y >= x
        for z in range(1, arg + 1) if z >= y and x * x + y * y == z * z
    ]

def solution6(arg):
    return [
        [j + i for j in arg[1]]
        for i in arg[0]
    ]

def solution7(arg):
    return [
        [j[i]  for j in arg]
        for i in range(len(arg[0]))
    ]
    # return list(map(list, zip(*arg)))

def solution8(arg):
    return [
        list(map(lambda x: int(x), i.split()))
        for i in arg
    ]

def solution9(arg):
    return {
        chr(i + 97): i ** 2
        for i in arg
    }

def solution10(arg):
    return {
        i[0].upper() + i[1:].lower()
        for i in arg
        if len(i) > 3
    }

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


if __name__ == "__main__":
    print(solution1("python"))
    print(solution2("python"))
    print(solution3(range(16)))
    print(solution4([[1, 2, 3], [4, 5, 6, 7], [8, 9], [0]]))
    print(solution5(15))
    print(solution6(([0, 1, 2], [0, 1, 2, 3, 4])))
    print(solution7([[1, 2], [3, 4], [5, 6]]))
    print(solution7([[1, 3, 5], [2, 4, 6]]))
    print(solution8(["0", "1 2 3", "4 5 6 7", "8 9"]))
    print(solution9(range(0, 7)))
    print(solution10(['Alice', 'vova', 'ANTON', 'Bob', 'kAMILA', 'CJ', 'ALICE', 'Nastya']))
