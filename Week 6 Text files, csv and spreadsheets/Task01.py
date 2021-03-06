# Ученые нашли табличку с текстом на языке племени Мумба-Юмба. Определите, сколько различных слов содержится в этом
# тексте. Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим
# числом пробелов или символами конца строки. Большие и маленькие буквы считаются различными.
#
# В этой и последующих задачах этого занятия вам нужно скачать файл по ссылке, запустить свой скрипт на собственном
# компьютере и ввести только ответ конкретно для этого файла.

f_in = open('inputs/input01.txt', 'r', encoding='utf8')

all_words = set()

for line in f_in:
    all_words.update(line.split())

print(len(all_words))

f_in.close()
