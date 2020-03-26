# В этой задаче достаточно обернуть в функцию то, что делает предыдущая и вызвать подсчет числа внутренних ссылок для
# двух статей: https://stepik.org/media/attachments/lesson/258943/Moscow.html и
# https://stepik.org/media/attachments/lesson/258944/New-York.html
#
# В качестве ответа на задачу введите два числа через пробел.

from urllib.request import urlopen

from bs4 import BeautifulSoup


def get_int_links(link):
    resp = urlopen(link)
    html = resp.read().decode('utf8')
    sp = BeautifulSoup(html, 'html.parser')

    results = []

    for link in sp.find_all('a'):
        if link.has_attr('href'):
            addr = link.get('href')
            if not (addr.startswith('http') or addr.startswith('#') or addr.startswith('//')) and ':' not in addr:
                results.append(addr)

    return results


Moscow_links = get_int_links('https://stepik.org/media/attachments/lesson/258943/Moscow.html')
NY_links = get_int_links('https://stepik.org/media/attachments/lesson/258944/New-York.html')

print(len(Moscow_links), len(NY_links))
