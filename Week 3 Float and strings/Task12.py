# В первой строке задается строка string
#
# Во второй строке задается строка substring
#
# Выведите True, если строка string начинается с подстроки substring, и False в противном случае
#
# Подсказка: для этого есть готовый метод

s = input()
subs = input()
if s.find(subs) == 0:
    print(True)
else:
    print(False)
