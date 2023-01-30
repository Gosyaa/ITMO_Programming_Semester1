cyrillic_low = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
d = {c: c for c in cyrillic_low}
d["а"] = 'a'
d["б"] = 'b'
d["в"] = 'v'
d["г"] = 'g'
d["д"] = 'd'
d["е"] = 'e'
d["ё"] = 'e'
d["ж"] = 'zh'
d["з"] = 'z'
d["и"] = 'i'
d["й"] = 'y'
d["к"] = 'k'
d["л"] = 'l'
d["м"] = 'm'
d["н"] = 'n'
d["о"] = 'o'
d["п"] = 'p'
d["р"] = 'r'
d["с"] = 's'
d["т"] = 't'
d["у"] = 'u'
d["ф"] = 'f'
d["х"] = 'kh'
d["ц"] = 'ts'
d["ч"] = 'ch'
d["ш"] = 'sh'
d["щ"] = 'shch'
d["ы"] = 'y'
d["э"] = 'e'
d["ю"] = 'yu'
d["я"] = 'ya'
s = input()
ans = ''
for c in s:
    if c in cyrillic_low:
        ans = ans + d[c]
    else:
        ans = ans + c
print(ans)