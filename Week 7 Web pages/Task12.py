# В этой задаче достаточно вам необходимо посчитать количество внутренних ссылок, которые есть в обеих статьях:
# https://stepik.org/media/attachments/lesson/258943/Moscow.html
# и
# https://stepik.org/media/attachments/lesson/258944/New-York.html
#
# Обратите внимание, что если ссылка встречается в статье несколько раз, то учитывать ее нужно лишь однажды, т.е.
# необходимо найти количество различных страниц википедии, на которых есть ссылка как из первой, так и из второй статьи.

from urllib.request import urlopen

from bs4 import BeautifulSoup


def get_int_links(link):
    resp = urlopen(link)
    html = resp.read().decode('utf8')
    sp = BeautifulSoup(html, 'html.parser')

    results = set()

    for link in sp.find_all('a'):
        if link.has_attr('href'):
            addr = link.get('href')
            if not (addr.startswith('http') or addr.startswith('#') or addr.startswith('//')) and ':' not in addr:
                results.add(addr)

    return results


Moscow_links = get_int_links('https://stepik.org/media/attachments/lesson/258943/Moscow.html')
NY_links = get_int_links('https://stepik.org/media/attachments/lesson/258944/New-York.html')

print(len(Moscow_links & NY_links))
