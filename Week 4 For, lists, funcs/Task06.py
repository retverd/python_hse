# В первой строке вводится строка-разделитель.
#
# Во второй строке вводится текст, состоящий из слов, разделенных пробелом.
#
# Выведите слова из текста, разделяя их строкой-разделителем.

sep = input()
myStr = input()

print(myStr.replace(' ', sep), end="")
