# Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES (в отдельной
# строке), если это число ранее встречалось в последовательности или NO, если не встречалось.

mylist = list(map(int, input().split()))
myset = set()

for val in mylist:
    if val in myset:
        print('YES')
    else:
        print('NO')
    myset.add(val)
