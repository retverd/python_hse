# Вам дана область карты https://stepik.org/media/attachments/lesson/266078/mapcity.osm
#
# Пройдите по всем way в этой области, выделите среди них замкнутые (те, у которых совпадает ссылка на первый и
# последний node), среди всех замкнутых выделите те, у которых установлен tag с ключом building и произвольным
# значением.
#
# Для каждого подходящего под условия way выведите две строки. В первой укажите одно число - id этого way. Во второй
# перечислите через пробел id (ref) всех nd, входящих в этот way в том же порядке, в котором они перечисляются в файле.
#
# Выводить ответы для подходящих way нужно в том порядке, в котором они встречаются во входном файле

import xml.etree.ElementTree as ET
import requests

# tree = ET.fromstring(requests.get('https://stepik.org/media/attachments/lesson/266078/mapcity.osm').text)
tree = ET.fromstring(open("inputs/input11-15.osm", 'r', encoding='utf8').read())


def get_nds_ref(nds_list):
    nds_refs = []
    for nd in nds_list:
        nds_refs.append(nd.attrib['ref'])
    return nds_refs


for way in tree.findall("way/tag[@k='building']/.."):
    nds = way.findall('nd')
    if nds[0].attrib['ref'] == nds[len(nds) - 1].attrib['ref']:
        print(way.attrib['id'])
        print(*get_nds_ref(nds))
