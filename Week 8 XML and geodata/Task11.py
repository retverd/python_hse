# Вам дана область карты https://stepik.org/media/attachments/lesson/266078/mapcity.osm
#
# Пройдите по первым ста node в этой области и выведите для каждого три числа: id, широту (атрибут lat) и долготу
# (атрибут lon).
#
# Числа для каждого node выводите в отдельной строке, разделяя одним пробелом. Обрабатывать node нужно в том же порядке,
# в котором они встречаются во входном файле.

import xml.etree.ElementTree as ET
import requests

# tree = ET.fromstring(requests.get('https://stepik.org/media/attachments/lesson/266078/mapcity.osm').text)
tree = ET.fromstring(open("inputs/input11-15.osm", 'r', encoding='utf8').read())

i = 0
max_i = 100

for node in tree.findall("node"):
    if i == max_i:
        break
    print(node.attrib['id'], node.attrib['lat'], node.attrib['lon'])
    i += 1
