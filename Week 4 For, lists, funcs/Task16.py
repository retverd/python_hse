# Напишите функцию sort3, которая принимает 3 параметра a, b, c, переставляет их так чтобы и возвращает тройку
# чисел a <= b <= c.
#
# Дано три числа по одному в строке. Воспользуйтесь функцией sort3 чтобы упорядочить эти три числа.


def sort3(x, y, z):
    if x > y:
        x, y = y, x
    if x > z:
        x, z = z, x
    if y > z:
        y, z = z, y
    return " ".join(map(str, [x, y, z]))


print(sort3(int(input()), int(input()), int(input())))
