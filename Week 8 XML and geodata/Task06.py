# В OpenStreetMap XML встречаются теги way, которые соответствуют некоторым линиям и многоугольникам на карте.
# Way состоит из списка нодов (точек), которые задаются тегами nd вложенными в тег way. Для доступного по ссылке
# https://stepik.org/media/attachments/lesson/245681/map2.osm определите id того way, который содержит в себе
# наибольшее количество нодов. Если таких несколько - выведите тот id, который встречается в файле раньше.

import xml.etree.ElementTree as ET
import requests

tree = ET.fromstring(requests.get('https://stepik.org/media/attachments/lesson/245681/map2.osm').text)
ways = {}

for way in tree.findall("way"):
    way_id = way.attrib['id']
    if way_id in ways:
        print(f'Error with id {way_id}')
    else:
        ways[way_id] = len(way.findall("nd"))

v = list(ways.values())
k = list(ways.keys())

print(k[v.index(max(v))])
