# В этой задаче вам предстоит изучить, как устроен XML для описания объектов OpenStreetMap. Вручную откройте скаченный
# файл с помощью текстового редактора и найдите в нём тэг tag с атрибутом k="public_transport" в node с id равным
# 203573042 (удобно поискать это число поиском в текстовом редакторе).
#
# В качестве ответа необходимо ввести содержимое атрбута v для найденного тэга tag без кавычек.

import xml.etree.ElementTree as ET
import requests

tree = ET.fromstring(requests.get('https://stepik.org/media/attachments/lesson/266068/map2.osm').text)

print(tree.find(".//node[@id='203573042']/tag[@k='public_transport']").attrib['v'])
