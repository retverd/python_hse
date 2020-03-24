# В качестве ответа введите все строки наибольшей длины из входного файла, не меняя их порядок.
#
# В данной задаче удобно считать список строк входного файла целиком при помощи метода readlines().

f_in = open('inputs/input06.txt', 'r', encoding='utf8')

lines = f_in.readlines()
lines_num = {}

for line in lines:
    l_len = len(line)
    if l_len not in lines_num:
        lines_num[l_len] = []
    lines_num[l_len].append(line)

max_l = max(lines_num)

for line in lines_num[max_l]:
    print(line, end='')

f_in.close()
