# Определите количество четных элементов в последовательности, завершающейся числом 0.
#
# Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит,
# а служит как признак ее окончания).

even_count = 0
i = int(input())

while i != 0:
    if i % 2 == 0:
        even_count += 1
    i = int(input())

print(even_count)
