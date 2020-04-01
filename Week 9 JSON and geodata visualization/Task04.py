# Вам дан xlsx-файл с информацией о спортивных площадках в Москве. Вам необходимо сдать на проверку json-файл, в котором
# будет храниться один словарь, ключами которого будут административные округа (AdmArea), а значениями словари,
# в которых, в свою очередь, ключами будут названия районов (District), относящихся к этому административному округу,
# а значениями - списки адресов площадок (Address) в том порядке, в котором они встречались в исходном файле..

import json
import pandas as pd

output_data = {}

input_data = pd.read_excel('inputs/input04.xlsx', sheet_name='Sheet0', index_col=0)

for row in input_data.itertuples():
    if row.AdmArea not in output_data:
        output_data[row.AdmArea] = {}
    if row.District not in output_data[row.AdmArea]:
        output_data[row.AdmArea][row.District] = []
    output_data[row.AdmArea][row.District].append(row.Address)

f_out = open('outputs/output04.json', 'w', encoding='utf-8')
json.dump(output_data, f_out, ensure_ascii=False)
f_out.close()
