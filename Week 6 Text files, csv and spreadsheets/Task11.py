# Вася составил таблицу с ценами на продукты в разных магазинах. В первой строке таблицы (кроме первой ячейки) записаны
# названия продуктов. Во всех строках, начиная со второй, записана информация о ценах в магазине. В первой ячейки
# написано название магазина, а в ячейках, начиная со второй - цена на товар, название которого записано в первой строке
# соответствующего столбца.
#
# Таблица задана как csv-файл, разделителем ячеек выступает точка с запятой, а строковые константы не окружаются
# кавычками.
#
# Вася очень хочет поесть, но денег у него мало. Поэтому помогите ему определить самый дешевый продукт и в каком
# магазине он продается. Название продукта следует записать в первой строке, а название магазина - во второй. Если
# несколько товаров стоят одинаково, то выведите то название, которое раньше в алфавитном порядке. Если этот товар
# продается в нескольких магазинах по одной минимальной цене, то выведите минимальное в алфавитном порядке название
# магазина.

f_in = open('inputs/input11.csv', 'r', encoding='utf8')

min_price = 999
tgt_vals = {}
flag = True

for line in f_in:
    if flag:
        goods = line[line.find(";") + 1:line.find("\n")].split(';')
        flag = False
    else:
        shop = line[:line.find(";")]
        spl_line = list(map(int, line[line.find(";") + 1:line.find("\n")].split(';')))
        min_price = min(min_price, min(spl_line))
        if min_price in spl_line:
            if min_price not in tgt_vals:
                tgt_vals[min_price] = {}
            for i, x in enumerate(spl_line):
                if x == min_price:
                    if goods[i] not in tgt_vals[min_price]:
                        tgt_vals[min_price][goods[i]] = [shop]
                    else:
                        tgt_vals[min_price][goods[i]].append(shop)

good = sorted(tgt_vals[min_price])[0]

print(good)
print(sorted(tgt_vals[min_price][good])[0])

f_in.close()
