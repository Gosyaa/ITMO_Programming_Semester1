n = int(input())
a = [True]
for i in range(1, n + 1):
    a.append(True)
a[1] = False
i = 2
while i * i < n:
    if a[i] == True:
        k = i + i
        while k <= n:
            a[k] = False
            k += i
    i += 1
for i in range(2, n + 1):
    if a[i] == True:
        print(i, end=' ')