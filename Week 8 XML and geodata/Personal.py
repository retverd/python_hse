# Вывести по заданной области все магазины в структуре тип->название->количество(по названию)-> количество(по типу).
# Сортировка: уровень 1 - по алвафитному порядку названий, уровень 2 - по количеству магазинов (по убыванию), и по
# названию (в алфавитном порядке).
# Примечание: выяснилось, что не у всех магазинов указано название, поэтому в качестве альтернативы ищется tag с ключом
# brand

import xml.etree.ElementTree as ET


def f(x):
    return -x[1], x[0]


tree = ET.parse('inputs/map.osm')
shops = {}

for shop in tree.findall("node/tag[@k='shop']/.."):
    shop_type = shop.find("tag[@k='shop']").get('v')
    tagName = shop.find("tag[@k='name']")
    if tagName is None:
        tagBrand = shop.find("tag[@k='brand']")
        if tagBrand is None:
            shop_name = "Unknown"
        else:
            shop_name = tagBrand.get('v')
    else:
        shop_name = tagName.get('v')

    if shop_type in shops:
        if shop_name in shops[shop_type]:
            shops[shop_type][shop_name] += 1
        else:
            shops[shop_type][shop_name] = 1
    else:
        shops[shop_type] = {}
        shops[shop_type][shop_name] = 1

ordered_shops = sorted(shops.items())

for shop_type in ordered_shops:
    print(f'Тип: {shop_type[0]}')
    count = 0

    for shop_name in sorted(shop_type[1].items(), key=f):
        print(f'\t{shop_name[0]}: {shop_name[1]}')
        count += shop_name[1]
    print(f'Итого {count} магазинов этого типа.')
