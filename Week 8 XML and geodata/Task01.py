# В этой задаче вам предстоит изучить, как устроен XML для описания объектов OpenStreetMap. Вручную откройте скаченный
# файл с помощью текстового редактора и найдите в нём широту (атрибут lat) для тега node с id равным 6428535115
# (удобно поискать это число поиском в текстовом редакторе).
#
# В качестве ответа необходимо ввести содержимое параметра lat без кавычек (вещественное число с 7 знаками после точки).

import xml.etree.ElementTree as ET
import requests

tree = ET.fromstring(requests.get('https://stepik.org/media/attachments/lesson/266068/map2.osm').text)

print(tree.find(".//node[@id='6428535115']").attrib['lat'])
