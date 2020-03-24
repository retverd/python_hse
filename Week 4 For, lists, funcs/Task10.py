# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

strval = input()
# strval = "1 5 2 4 3"

lst = strval.split(" ")
prev = int(lst[0])

for s in lst[1:]:
    if int(s) > prev:
        print(s, end=" ")
    prev = int(s)

print()
