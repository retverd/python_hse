# Скачайте с помощью скрипта область карты OSM, где минимальная широта равна 55.5586, минимальная долгота 37.5649,
# максимальная широта 55.5728, максимальная долгота 37.5803.
#
# Чтобы вспомнить, как добыть адрес api, который возвращает вам нужный кусок карты, пройдите по ссылке
# https://www.openstreetmap.org/export, включите режим разработчика в браузере (ctrl+shift+i), откройте вкладку
# "Network", затем выберите слева Manually select a different area, выберите какую-нибудь область и нажмите кнопку
# Export. Во вкладке Network появится адрес ссылки, по которой добывается xml файл. Исправьте в нем координаты на данные
# в условии задачи и вы получите адрес того файла, который нужно сдать на проверку.

from urllib.request import urlretrieve

min_lat = 55.5586
min_lon = 37.5649
max_lat = 55.5728
max_lon = 37.5803

urlretrieve(f'https://www.openstreetmap.org/api/0.6/map?bbox={min_lon}%2C{min_lat}%2C{max_lon}%2C{max_lat}',
            'outputs/output10.osm')
