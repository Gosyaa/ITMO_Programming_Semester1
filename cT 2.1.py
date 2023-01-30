from random import randint
def gen(n):
    a = []
    for i in range(n):
        q = randint(0, 2)
        if q == 0:
            a.append(None)
        else:
            a.append(randint(-30, 30))
    return a
def sum(a):
    ans = 0
    for i in a:
        ans += i
    return ans
a = gen(15)
print(*a)
a = list(filter(lambda x: x != None, a))
print(*a)
print(round(sum(a) / len(a), 2))