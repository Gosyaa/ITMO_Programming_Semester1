import sys
def dist(a, b):
    ans = ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5
    return ans
def triangle(a, b, c):
    l1 = dist(a, b)
    l2 = dist(b, c)
    l3 = dist(a, c)
    p = (l1 + l2 + l3) / 2
    s = (p * (p - l1) * (p - l2) * (p - l3))**0.5
    return s
print('Введите координаты вершин правильного 5-тиугольника')
a = []
for i in range(5):
    x, y = map(float, input().split())
    a.append((x, y))
l = 10**10
d = 0
for i in range(1, 5):
    l = min(l, dist(a[0], a[i]))
    d = max(d, dist(a[0], a[i]))
q = (l * (5**0.5 + 1)) / 2
for i in range(5):
    for j in range(i + 1, 5):
        if dist(a[i], a[j]) == l:
            a[i + 1], a[j] = a[j], a[i + 1]
            break
s = triangle(a[0], a[-1], a[1]) + triangle(a[1], a[2], a[3]) + triangle(a[1], a[3], a[4])
print(round(s, 2))