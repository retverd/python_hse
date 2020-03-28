# Вам дана область карты https://stepik.org/media/attachments/lesson/266078/mapcity.osm
#
# Пройдите по всем way в этой области, выделите среди них замкнутые (те, у которых совпадает ссылка на первый и
# последний node), среди всех замкнутых выделите те, у которых установлен tag с ключом building и произвольным
# значением.
#
# Для каждого подходящего под условия way выведите две строки. В первой укажите одно число - id этого way. Во второй
# выведите список кортежей, содержащих координаты (широту и долготу) всех node, входящих в этот way. Для этого удобно в
# первой задаче к предыдущему видео сохранить все координаты в словарь, где ключом явлеятся id нода, и совместить ее с
# последней задачей к предыдущему видео.
#
# Выводить ответы для подходящих way нужно в том порядке, в котором они встречаются во входном файле

import xml.etree.ElementTree as ET
import requests

# tree = ET.fromstring(requests.get('https://stepik.org/media/attachments/lesson/266078/mapcity.osm').text)
tree = ET.fromstring(open("inputs/input11-15.osm", 'r', encoding='utf8').read())


def get_nds_coords(doc_tree, nds_list):
    nds_coords = []
    attrib = 'ref'
    for nd in nds_list:
        node = doc_tree.find(f'node[@id="{nd.attrib[attrib]}"]')
        nds_coords.append((float(node.attrib["lat"]), float(node.attrib["lon"])))
    return nds_coords


for way in tree.findall("way/tag[@k='building']/.."):
    nds = way.findall('nd')
    if nds[0].attrib['ref'] == nds[len(nds) - 1].attrib['ref']:
        print(way.attrib['id'])
        print(get_nds_coords(tree, nds))
