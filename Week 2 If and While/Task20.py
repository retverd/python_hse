# Даны два целых числа A и B (при этом A≤B). Выведите все числа от A до B включительно.
#
# Формат ввода
# Вводятся два целых числа.
#
# Формат вывода
# Выведите ответ на задачу.

a = int(input())
b = int(input())
i = a
while i <= b:
    print(i, end=" ")
    i += 1
