# Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей и выведите
# количество таких элементов.

strval = input()
# strval = "1 5 1 5 1 6 2"

lst = strval.split(" ")
strlen = len(lst) - 1
i = 1
c = 0

while i < strlen:
    if int(lst[i]) > int(lst[i + 1]) and int(lst[i]) > int(lst[i - 1]):
        c += 1
    i += 1

print(c)
