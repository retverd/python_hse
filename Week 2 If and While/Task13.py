# По данному целому числу N распечатайте все квадраты натуральных (целых, положительных) чисел, не превосходящие N, в
# порядке возрастания. Обратите внимание, что если N является полным квадратом, то его тоже нужно печатать.

x = int(input())
i = 1
pow_i = i ** 2

while pow_i <= x:
    print(pow_i)
    i = i + 1
    pow_i = i ** 2
