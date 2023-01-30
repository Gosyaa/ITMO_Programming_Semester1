m = int(input())
if m <= 2 or m == 12:
    print('Winter')
elif 3 <= m <= 5:
    print('Spring')
elif 6 <= m <= 8:
    print('Summer')
elif 9 <= m <= 11:
    print('Fall')
else:
    print('Error')