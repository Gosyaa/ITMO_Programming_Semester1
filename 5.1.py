def fib(n):
    if n == 1 or n == 2:
        return 1
    a = [0 for i in range(n)]
    a[0] = 0
    a[1] = 1
    for i in range(2, n):
        a[i] = a[i - 2] + a[i - 1]
    return a[n - 1]
a = int(input())
print(fib(a))    