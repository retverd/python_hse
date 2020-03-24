# В первой строке задаётся количество названий столиц и государств - число N. В следующих N строках задаются названия
# столиц и государств по одному в строке, слова разделяются одним пробелом. Отсортируйте названия столиц и государств
# по названию государства в алфавитном порядке и выведите их по одному в строке.


def my_key(x):
    return x[1]


numb = int(input())
my_list = []
i = 0

while i < numb:
    my_list.append(input().split())
    i += 1

newlist = sorted(my_list, key=my_key)

for val in newlist:
    print(*val)
