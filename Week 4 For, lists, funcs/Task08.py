# Выведите все четные элементы списка.

str = map(int, input().split())

for s in str:
    if s % 2 == 0:
        print(s, end=" ")
