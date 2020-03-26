# Выведите все четные элементы списка.

myStr = map(int, input().split())

for s in myStr:
    if s % 2 == 0:
        print(s, end=" ")
