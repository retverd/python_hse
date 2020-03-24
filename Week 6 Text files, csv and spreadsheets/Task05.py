# Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк. Выведите три найденных числа в формате,
# приведенном в примере. Словом считается последовательность больших и маленьких латинских букв (для проверки того,
# состоит ли строка только из латинских букв удобно пользоваться методом isalpha()). Все остальные символы считаются
# разделителями слов.

import re

f_in = open('inputs/input05.txt', 'r', encoding='utf8')

letters = 0
words = 0
non_alph = re.compile('[^a-zA-Z ]')
whites = re.compile('[ ]')

lines = f_in.readlines()

for line in lines:
    line = non_alph.sub(' ', line)
    words += len(line.split())
    letters += len(whites.sub('', line))

print('Input file contains:')
print(f'{letters} letters')
print(f'{words} words')
print(f'{len(lines)} lines')

f_in.close()
