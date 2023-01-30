import string
s = list(input())
for i in range (len(s)):
    if s[i] in string.ascii_lowercase:
        s[i] = s[i].upper()
    else:
        s[i] = s[i].lower()
print(*s, sep = '')
