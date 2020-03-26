# Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит статью с Википедии про язык Python.
# В этой статье есть теги code, которыми выделяются конструкции на языке Python. Вам нужно найти все строки,
# содержащиеся между тегами <code> и </code> и найти те строки, которые встречаются чаще всего и вывести их в
# алфавитном порядке, разделяя пробелами.

from urllib.request import urlopen

from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/209719/2.html')
html = resp.read().decode('utf8')
sp = BeautifulSoup(html, 'html.parser')

results = {}

for code in sp.find_all('code'):
    if code.text in results:
        results[code.text] += 1
    else:
        results[code.text] = 1

max_freq = max(results.values())

max_keys = [k for k, v in results.items() if v == max_freq]

print(*max_keys)
