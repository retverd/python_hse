# По введенному целому положительному числу N посчитайте N! (N факториал).
#
# Фавториалом числа N называется произведение всех чисел от 1 до N.

a = int(input())
y = 1

for i in range(a):
    y *= (i + 1)

print(y)