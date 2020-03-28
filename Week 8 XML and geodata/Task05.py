# В OpenStreetMap XML встречаются теги node, которые соответствуют некоторым точкам на карте. Ноды могут не только
# обозначать какой-то точечный объект, но и входить в состав way (некоторой линии, возможно замкнутой) и не иметь
# собственных тегов. Для доступного по ссылке https://stepik.org/media/attachments/lesson/245681/map2.osm фрагмента
# карты посчитайте, сколько всего тегов node не содержат в себе ни одного тега tag (первое число в ответе), а сколько
# содержит хотя бы один тег tag (второе число в ответе). Числа введите через пробел.

import xml.etree.ElementTree as ET
import requests

tree = ET.fromstring(requests.get('https://stepik.org/media/attachments/lesson/245681/map2.osm').text)
none_count = 0
not_none_count = 0

for node in tree.findall("node"):
    if node.find("tag") is None:
        none_count += 1
    else:
        not_none_count += 1

print(none_count, not_none_count)
