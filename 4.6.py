import string
k = 0
while True:
    a = input()
    b = True
    for c in a:
        if not(c in string.digits):
            b = False
            break
    if b:
        k += 1
    else:
        break
print(k)