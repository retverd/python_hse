# В форме интернет-магазина пользователю нужно ввести свой номер телефона. Номер телефона состоит из 10 цифр, однако
# некоторые пользователи вводят его в формате +7123456789, некоторые - 8123456789, а некоторые и вовсе вводят только
# 9 цифр (без первой) 123456789.
#
# Вам необходимо привести номер к стандарту +7123456789

s = input()

if len(s) == 9:
    print("+7", s, sep="")
elif s.find("8") == 0:
    print("+7", s[1:], sep="")
else:
    print(s)
