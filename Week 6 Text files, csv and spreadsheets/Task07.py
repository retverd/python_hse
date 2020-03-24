# Выведите в обратном порядке содержимое всего файла полностью. Для этого считайте файл целиком при помощи метода
# read().

f_in = open('inputs/input07.txt', 'r', encoding='utf8')

cont = f_in.read()

print(cont[::-1])

f_in.close()
