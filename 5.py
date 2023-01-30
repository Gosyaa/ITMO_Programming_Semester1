s = input().split()
k = 1
a = 0
q = 1
for i in range(len(s[0]) - 1, -1, -1):
    if s[0][i] == '-':
        q = -1
    else:
        a += (int(s[0][i]) * k)
        k *= 10
a *= q
c = s[1]
k = 1
b = 0
q = 1
for i in range(len(s[2]) - 1, -1, -1):
    if s[2][i] == '-':
        q = -1
    else:
        b += (int(s[2][i]) * k)
        k *= 10
b *= q
ans = 0
f = True
if c == '+':
    ans = a + b
elif c == '-':
    ans = a - b
elif c == '*':
    ans = a * b
elif c == '/' and b != 0:
    ans = a / b
else:
    print('Error')
    f = False
if f:
    print(ans)