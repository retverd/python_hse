# Даны три целых числа. Найдите наибольшее из них (программа должна вывести ровно одно целое число).

a = int(input())
b = int(input())
c = int(input())
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
elif b > c:
    print(b)
else:
    print(c)
