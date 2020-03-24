# Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают все школьники и языки, которые
# знает хотя бы один из школьников.
#
# Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi, после каждого из чисел идет
# Mi строк, содержащих названия языков, которые знает i-й школьник.
#
# В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки - список таких
# языков, упорядоченный по алфавиту. Затем - количество языков, которые знает хотя бы один школьник, на следующих
# строках - список таких языков, упорядоченный по алфавиту.

tot_num = int(input())
if tot_num > 0:
    pups = list()

    for i in range(tot_num):
        j = int(input())
        tmp_set = set()
        for k in range(j):
            tmp_set.add(input())
        pups.append(tmp_set)

    inter = pups[0].copy()
    un = pups[0].copy()

    for i in range(1, len(pups)):
        inter.intersection_update(pups[i])
        un.update(pups[i])

    print(len(inter))
    if len(inter) > 0:
        print(*sorted(inter), sep="\n")
    print(len(un))
    if len(un) > 0:
        print(*sorted(un), sep="\n")
