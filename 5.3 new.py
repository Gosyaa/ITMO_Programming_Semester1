import string
import sys
def error():
    print('Некоректный ввод')
    sys.exit()
def num(s):
    i = 0
    q = '+-*:'
    s1 = ''
    s2 = ''
    c = '`'
    while i < len(s) and (s[i] in string.digits or s[i] == '.' or s[i] == '-'):
        if s[i] == '-' and i != 0:
            break
        s1 += s[i]
        i += 1
    if len(s1) == 0:
        error()
    if s1[0] == '.' or s1[-1] == '.':
        error()
    try:
        a = float(s1)
    except ValueError:
        error()
    if i < len(s) and s[i] in q:
        c = s[i]
        i += 1
    else:
        error()
    while i < len(s) and (s[i] in string.digits or s[i] == '.' or s[i] == '-'):
        s2 += s[i]
        i += 1
    if len(s2) == 0:
        error()
    if s2[0] == '.' or s2[-1] == '.':
        error()
    try:
        b = float(s2)
    except ValueError:
        error()
    if c == '`':
        error()
    return(a, b, c)
def calc(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == ':':
        if b == 0:
            error()
        return a / b
while True:
    s = input()
    if s == 'q':
        break
    s = s.replace(' ', '')
    a, b, c = num(s)
    print(round(calc(a, b, c), 2))
print('Завершение работы калькулятора')