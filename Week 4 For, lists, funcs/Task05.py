# Вводится строка, состоящая из слов, разделенных одним пробелом. Выведите все слова по одному в строке
# (пробелы выводить не нужно).
#
# Эта задача удобно решается с помощью методов split и join. Напомним, что перевод строки обозначается как \n внутри
# строковой константы.

a = input()

print(a.replace(' ', '\n'), end="")
