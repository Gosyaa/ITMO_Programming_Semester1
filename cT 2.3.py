def pow(a, b):
    if b < 0:
        a = 1 / a
        b = -b
    ans = 1
    for i in range(b):
        ans *= a
    return ans
def powrec(a, b):
    if b < 0:
        a = 1 / a
        b = -b
    if b == 0:
        return 1
    return a * powrec(a, b - 1)
a, b = map(int, input().split())
print(pow(a, b))
print(powrec(a, b))