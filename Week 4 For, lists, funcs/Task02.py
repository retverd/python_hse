# Вводится число целое положительное число N. Напечатайте все N-значные нечетные целые положительные числа в порядке
# убывания. Например, если вводится число 3, то необходимо печать трёхзначные числа (состоящие из трех цифр).
#
# Подсказка: Вспомните про возведение 10 в степень.

a = int(input())

for i in range(10 ** a - 1, 10 ** (a - 1) - 1, -2):
    print(i, end=" ")