# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.

strval = input()
# strval = "1 3 5 7"

lst = list(map(int, strval.split()))
minval = lst[0]
maxvalnum = 0
maxval = lst[0]
minvalnum = 0

for i in range(len(lst)):
    if lst[i] < minval:
        minval = lst[i]
        minvalnum = i
    if lst[i] > maxval:
        maxval = lst[i]
        maxvalnum = i

lst[minvalnum], lst[maxvalnum] = lst[maxvalnum], lst[minvalnum]
print(*lst)
