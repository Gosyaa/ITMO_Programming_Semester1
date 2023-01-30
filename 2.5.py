x, y = map(int, input('Введите координаты точки: ').split())
#print(x, y)
if x == 0 and y == 0:
    print('0, 0')
elif x == 0:
    print('Ox')
elif y == 0:
    print('Oy')
if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
if x < 0:
    if y > 0:
        print(2)
    else:
        print(3)