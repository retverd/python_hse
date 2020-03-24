# Вася планирует карьеру и переезд. Для это составил таблицу, в которой для каждого региона записал зарплаты для разных
# интересные ему профессий. Выведите название региона с самой высокой медианной зарплатой (медианой называется элемент,
# стоящий в середине массива после его упорядочивания) и, через пробел, название профессии с самой высокой средней
# зарплатой по всем регионам.

import pandas as pd

stat = pd.read_excel('inputs/input14.xlsx')

median_sal = stat.median(axis=1)
avr_sal = stat.mean()

print(stat[stat.columns[0]][median_sal.idxmax()], avr_sal.idxmax())
