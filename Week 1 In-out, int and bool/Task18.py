# Вася делает ремонт на кухне размером X на Y метров и хочет положить настенную плитку. Сколько квадратных метров плитки
# нужно купить Васе, если высота стен на кухне равна Z?
#
# Числа X, Y и Z задаются по одному в строке.

x = int(input())
y = int(input())
z = int(input())

print((2 * x + 2 * y) * z)
