# Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.

myset1 = set(map(int, input().split()))
myset2 = set(map(int, input().split()))

print(len(myset1.intersection(myset2)))
