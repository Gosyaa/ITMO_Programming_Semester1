from random import randint
a = randint(1, 100)
shots = 10
vic = False
while shots > 0:
    n = int(input('Угадайте число от 1 до 100: '))
    if n > a:
        print('Неверно, загаданное число меньше!')
    elif n < a:
        print('Неверно, загаданное число больше!')
    else:
        vic = True
        break
    shots -= 1
if vic:
    print('ВЫ ПОБЕДЕЛИ!!!!!!')
else:
    print('Вы проиграли. Попробуйте снова, правильный ответ', a)