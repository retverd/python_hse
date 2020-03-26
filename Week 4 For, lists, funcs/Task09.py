# Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
# Если наибольших элементов несколько, выведите индекс первого из них.

myStr = input()

lst = myStr.split(" ")
maxVal = int(lst[0])
idx = 0
i = 0

for s in lst:
    if int(s) > maxVal:
        maxVal = int(s)
        idx = i
    i += 1

print(maxVal, idx)
