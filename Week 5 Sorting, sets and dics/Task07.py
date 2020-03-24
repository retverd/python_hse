# Даны два списка чисел. Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.

myset1 = set(map(int, input().split()))
myset2 = set(map(int, input().split()))

print(*sorted(myset1.intersection(myset2)))
