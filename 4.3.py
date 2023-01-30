import string
s = input()
ans = 0
for c in s:
    if c in string.digits:
        ans += int(c)
print(ans)