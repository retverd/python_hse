# Главный бухгалтер компании "Рога и копыта" случайно удалил ведомость с начисленной зарплатой. К счастью, у него
# сохранились расчётные листки всех сотрудников. Помогите по этим расчётным листкам восстановить зарплатную ведомость.
# Архив с расчётными листками доступен по ссылке https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip
# (вы можете скачать и распаковать его вручную или самостоятельно научиться делать это с помощью скрипта на Питоне).
#
# Ведомость должна содержать 1000 строк, в каждой строке должно быть указано ФИО сотрудника и, через пробел, его
# зарплата. Сотрудники должны быть упорядочены по алфавиту.

import zipfile

import openpyxl

archive = zipfile.ZipFile('inputs/input13.zip', 'r')

summary = []
for file in zipfile.ZipFile.namelist(archive):
    wb = openpyxl.load_workbook(archive.open(file))
    sh = wb.active
    summary.append((sh['B2'].value, sh['D2'].value))

summary.sort()

for record in summary:
    print(record[0], record[1])
