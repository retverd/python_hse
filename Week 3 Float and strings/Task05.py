# Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада. Вклад составляет
# X рублей Y копеек. Определите размер вклада через год.
#
# Программа получает на вход целые числа P, X, Y.
#
# Программа должна вывести два числа: величину вклада через год в рублях и копейках. Дробная часть копеек отбрасывается.

p = int(input())
x = int(input())
y = int(input())

t = (x * 100 + y) * (100 + p)

print(t // 10000, (t // 100) % 100)
