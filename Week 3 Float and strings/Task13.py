# Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.

myStr = input()
s = "h"
sNew = "H"

start = myStr[:myStr.find(s) + 1]
end = myStr[myStr.rfind(s):]
middle = myStr[myStr.find(s) + 1:myStr.rfind(s)].replace(s, sNew)

print(start, middle, end, sep="")
