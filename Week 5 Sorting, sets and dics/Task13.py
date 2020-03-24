# Некоторый банк хочет внедрить систему управления счетами клиентов, поддерживающую следующие операции:
#
# Пополнение счета клиента. Снятие денег со счета. Запрос остатка средств на счете. Перевод денег между счетами
# клиентов. Начисление процентов всем клиентам.
#
# Вам необходимо реализовать такую систему. Клиенты банка идентифицируются именами (уникальная строка, не содержащая
# пробелов). Первоначально у банка нет ни одного клиента. Как только для клиента проводится операция пололнения, снятия
# или перевода денег, ему заводится счет с нулевым балансом. Все дальнейшие операции проводятся только с этим счетом.
# Сумма на счету может быть как положительной, так и отрицательной, при этом всегда является целым числом.
#
# Входной данные содержат количество и последовательность операций. Возможны следующие операции: DEPOSIT name sum -
# зачислить сумму sum на счет клиента name. Если у клиента нет счета, то счет создается. WITHDRAW name sum - снять
# сумму sum со счета клиента name. Если у клиента нет счета, то счет создается. BALANCE name - узнать остаток средств
# на счету клиента name. TRANSFER name1 name2 sum - перевести сумму sum со счета клиента name1 на счет клиента name2.
# Если у какого-либо клиента нет счета, то ему создается счет. INCOME p - начислить всем клиентам, у которых открыты
# счета, pот суммы счета. Проценты начисляются только клиентам с положительным остатком на счету, если у клиента остаток
# отрицательный, то его счет не меняется. После начисления процентов сумма на счету остается целой, то есть начисляется
# только целое число денежных единиц. Дробная часть начисленных процентов отбрасывается.
#
# Для каждого запроса BALANCE программа должна вывести остаток на счету данного клиента. Если же у клиента
# с запрашиваемым именем не открыт счет в банке, выведите ERROR.


def balance(details):
    global clients
    if details in clients:
        print(clients[details])
    else:
        print("ERROR")
    return


def deposit(details):
    global clients
    my_args = list(details.split())
    if my_args[0] not in clients:
        clients[my_args[0]] = 0
    clients[my_args[0]] += int(my_args[1])
    return


def withdraw(details):
    global clients
    my_args = list(details.split())
    if my_args[0] not in clients:
        clients[my_args[0]] = 0
    clients[my_args[0]] -= int(my_args[1])
    return


def transfer(details):
    global clients
    my_args = list(details.split())
    withdraw(my_args[0] + " " + my_args[2])
    deposit(my_args[1] + " " + my_args[2])
    return


def income(details):
    global clients
    perc = int(details)
    for client in clients:
        if clients[client] > 0:
            clients[client] += clients[client] * perc // 100
    return


total = int(input())
acc_act = {"deposit", "withdraw", "balance", "transfer", "income"}

clients = {}
for i in range(total):
    command = input()
    action = command[:command.find(" ")].lower()
    args = command[command.find(" ") + 1:]
    if action in acc_act:
        locals()[action](args)
