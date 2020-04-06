# Дана строка, в которой буква h встречается как минимум два раза. Разверните последовательность символов, заключенную
# между первым и последнием появлением буквы h, в противоположном порядке.

test_str = input()
char = 'h'

first_occ = test_str.find(char)
last_occ = test_str.rfind(char)

out_str = test_str[0:first_occ + 1] + test_str[last_occ - 1:first_occ:-1] + test_str[last_occ:]

print(out_str)
