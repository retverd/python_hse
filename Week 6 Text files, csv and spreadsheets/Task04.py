# Выведите все строки данного входного файла в обратном порядке. Для этого считайте список всех строк при помощи метода
# readlines().
#
# Последняя строка входного файла заканчивается символом '\n'.

f_in = open('inputs/input04.txt', 'r', encoding='utf8')
f_out = open('outputs/output04.txt', 'w', encoding='utf8')

all_lines = f_in.readlines().__reversed__()

f_out.writelines(all_lines)

f_in.close()
f_out.close()
