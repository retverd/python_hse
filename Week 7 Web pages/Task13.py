# В этой задаче достаточно вам необходимо найти все внутренние ссылки, которые есть в обеих статьях:
# https://stepik.org/media/attachments/lesson/258943/Moscow.html и
# https://stepik.org/media/attachments/lesson/258944/New-York.html и вывести их в алфавитном порядке по одной в строке.
#
# Обратите внимание, что если ссылка встречается в статье несколько раз, то учитывать ее нужно лишь однажды.

from urllib.request import urlopen

from bs4 import BeautifulSoup


def get_int_links(link_to_handle):
    resp = urlopen(link_to_handle)
    html = resp.read().decode('utf8')
    sp = BeautifulSoup(html, 'html.parser')

    results = set()

    for link_to_handle in sp.find_all('a'):
        if link_to_handle.has_attr('href'):
            addr = link_to_handle.get('href')
            if not (addr.startswith('http') or addr.startswith('#') or addr.startswith('//')) and ':' not in addr:
                results.add(addr)

    return results


Moscow_links = get_int_links('https://stepik.org/media/attachments/lesson/258943/Moscow.html')
NY_links = get_int_links('https://stepik.org/media/attachments/lesson/258944/New-York.html')

both_links = sorted(Moscow_links & NY_links)

for link in both_links:
    print(link)
