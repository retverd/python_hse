# По данным портала открытых данных Москвы определите количество дней, когда освещение включено 12 часов или более.

import json
from urllib.request import urlopen

api_key = "put_your_key_here"
list_id = 3288
exp_dur = 12
counter = 0

response = urlopen(f'https://apidata.mos.ru/v1/datasets/{list_id}/rows?api_key={api_key}').read().decode('utf-8')

parsedResp = json.loads(response)

for rec in parsedResp:
    dur = rec['Cells']['DurationOfLighting']
    if int(dur[:2]) >= exp_dur:
        counter += 1

print(counter)
