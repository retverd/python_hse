# Даны три целых числа A, B, C. Выведите YES, есть ли среди них хотя бы одно четное и хотя бы одно нечетное, и NO в
# противном случае.

a = int(input())
b = int(input())
c = int(input())
if a % 2 == 0:
    if b % 2 == 1 or c % 2 == 1:
        print("YES")
    else:
        print("NO")
elif b % 2 == 0 or c % 2 == 0:
    print("YES")
else:
    print("NO")
