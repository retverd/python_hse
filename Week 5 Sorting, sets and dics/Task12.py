# Дана строка. Выведите слово, которое в этой строке встречается чаще всего. Если таких слов несколько, выведите то,
# которое меньше в лексикографическом (алфавитном) порядке.

s = input()

my_list = list(s.split())
dict = {}

for val in sorted(my_list):
    if val in dict:
        dict[val] += 1
    else:
        dict[val] = 1

max_key = max(dict, key=dict.get)

print(max_key)
