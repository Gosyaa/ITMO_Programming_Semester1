from random import randint
def gen(n):
    a = []
    for i in range(n):
        a.append(randint(-100, 100))
    return a
def solve(a):
    a1 = list(filter(lambda x: x < 0, a))
    a1 = sorted(a1)
    a1 = a1[::-1]
    a2 = list(filter(lambda x: x >= 0, a))
    a2 = sorted(a2)
    return(a1, a2)
a = gen(10)
print(*a)
print(solve(a))