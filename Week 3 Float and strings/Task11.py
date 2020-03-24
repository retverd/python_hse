# В введенной строке необходимо заменить все буквы A на B, а все буквы B - на A. Заменять нужно только заглавные буквы.

s = input()
maketrans = s.maketrans
print(s.translate(maketrans('AB', 'BA')))
