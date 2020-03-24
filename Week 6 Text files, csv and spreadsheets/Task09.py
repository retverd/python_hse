# В csv-файле (разделитель - точка с запятой, кавычки не используются) содержится анонимизированная информация о
# зарплатах сотрудников в различных компаниях. В первом столбце записано название компании, а во втором - зарплата.
#
# Поменяйте местами первый и второй столбцы, по-прежнему разделяя значения в ячейках одной строки точкой с запятой.
# Сохраняйте порядок строк.

f_in = open('inputs/input09.csv', 'r', encoding='utf8')
f_out = open('outputs/output09.csv', 'w', encoding='utf8')

rev_lines = []

for line in f_in:
    rev_lines.append(line[line.find(";") + 1:line.find("\n")] + ";" + line[:line.find(";")] + "\n")

f_out.writelines(rev_lines)

f_in.close()
f_out.close()
