import string
def num(s):
    i = 0
    q = '+-*:'
    s1 = ''
    s2 = ''
    c = '`'
    while s[i] in string.digits or s[i] == '.':
        s1 += s[i]
        i += 1
    a = float(s1)
    while not (s[i] in string.digits):
        if s[i] in q and c == '`':
            c = s[i]
        i += 1
    while i < len(s) and (s[i] in string.digits or s[i] == '.'):
        s2 += s[i]
        i += 1
    b = float(s2)
    return (a, b, c)
def calc(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == ':':
        return a / b
while True:
    s = input()
    if s == 'q':
        break
    a, b, c = num(s)
    print(round(calc(a, b, c), 2))
print('Завершение работы калькулятора')