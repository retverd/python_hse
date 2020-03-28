# Вася решил открыть АЗС (заправку). Чтобы оценить уровень конкуренции он хочет изучить количество заправок в
# интересующем его районе. Вася скачал интересующий его кусок карты OSM
# https://stepik.org/media/attachments/lesson/245681/map2.osm и хочет посчитать, сколько на нём отмечено точечных
# объектов (node), являющихся заправкой. В качестве ответа вам необходимо вывести одно число - количество АЗС.
#
# Заправка в OSM обозначается парой ключ-значение amenity=fuel. Эта пара находится среди тегов tag внутри node.

import xml.etree.ElementTree as ET
import requests

tree = ET.fromstring(requests.get('https://stepik.org/media/attachments/lesson/245681/map2.osm').text)

gas_stations = tree.findall("node/tag[@k='amenity'][@v='fuel']/..")

print(len(gas_stations))
