for i in range(1000, 10000):
    s = {i // 1000, i // 100 % 10, i // 10 % 10, i % 10}
    if len(s) == 4:
        print(i, end = ' ')