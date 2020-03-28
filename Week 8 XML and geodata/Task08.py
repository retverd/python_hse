# Вася, открывший заправку в прошлой задаче, разорился. Конкуренция оказалась слишком большой. Вася предполагает, что
# это произошло от того, что теги заправки могут быть не только на точке, но и на каком-то контуре. Определите, сколько
# заправок на самом деле (не только обозначенных node, но и way) есть на фрагменте карты
# https://stepik.org/media/attachments/lesson/245681/map2.osm

import xml.etree.ElementTree as ET
import requests

tree = ET.fromstring(requests.get('https://stepik.org/media/attachments/lesson/245681/map2.osm').text)
# tree = ET.fromstring(open("inputs/input04-08.osm", 'r', encoding='utf8').read())

gas_stations = tree.findall(".//tag[@k='amenity'][@v='fuel']")

print(len(gas_stations))
