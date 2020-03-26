# Дана строка. Выведите слово, которое в этой строке встречается чаще всего. Если таких слов несколько, выведите то,
# которое меньше в лексикографическом (алфавитном) порядке.

s = input()

my_list = list(s.split())
myDict = {}

for val in sorted(my_list):
    if val in myDict:
        myDict[val] += 1
    else:
        myDict[val] = 1

max_key = max(myDict, key=myDict.get)

print(max_key)
