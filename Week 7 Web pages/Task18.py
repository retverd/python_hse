# В файле https://stepik.org/media/attachments/lesson/258944/New-York.html есть несколько таблиц, у которых атрибут
# class равен wikitable collapsible collapsed.
#
# Вам необходимо найти вторую (при нумерации с единицы) такую таблицу и преобразовать ее в csv-таблицу. В csv-таблице
# ячейки должны разделяться запятой, а строки не должны окружаться кавычками.
#
# Например, для таблицы:
#
# <table>
# <tr><td>a</td><td>b</td></tr>
# <tr><td colspan=2>c</td></tr>
# </table>
# ответ должен выглядеть так:
#
# a,b
# c
# Обратите внимание, что в таблице может встречаться тег <tbody>, на который мы можем просто не обращать внимания.
# Также там могут встречаться теги <th> (ячейка-заголовок), которые следует интерпретировать так же как теги <td>.
# Для поиска нескольких тегов удобно пользоваться методом find_all, которому в качестве параметра передается список
# строк с нужными названиями тегов.
#
# Чтобы получить содержимое тега td (то что записано от открывающего до закрывающего тега), достаточно написать td.text.
# Лучше удалить все пробельные символы в полученной строке с помощью метода strip().

from urllib.request import urlopen

from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/258944/New-York.html')
sp = BeautifulSoup(resp, 'html5lib')

tables = sp.find_all('table', class_='wikitable collapsible collapsed')
csv_row = []

for row in tables[1].find_all('tr'):
    for cell in row.find_all(['th', 'td']):
        text = cell.text.strip()
        if len(text) > 0:
            csv_row.append(text)
    if len(csv_row) > 0:
        print(','.join(csv_row))
        csv_row = []
