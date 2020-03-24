# Вася делает ремонт в комнате размером A на B метров с высотой стен C метров и хочет оклеить стены обоями. Обои
# \продаются в рулонах шириной 1 метр и длиной D метров. Какое минимальное количество рулонов необходимо купить Васе,
# чтобы обоев хватило на покрытие всей площади стен комнаты?
#
# Целые числа A, B, C и D задаются по одному в строке

l = int(input())
w = int(input())
h = int(input())
d = int(input())

sq = (2 * l + 2 * w) * h

print(((sq - 1) // d) + 1)
