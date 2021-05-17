# openpyxl - открытие экселя, re - регулярки, fuzzywuzzy - Расстояние Левенштейна
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import openpyxl
import re

#Создание пустых списков под заполнение данными из excel
inputData = []
storeData = []

#Список патернов для регулярных выражений
pattern1 = r'\b(\w+)[-\.,\\](\w+)\b'
pattern2 = r'(\w+)[-\.,\\_](\w+)[-\.,\\_](\w+)'
pattern3 = r'(\w+)[-\.,\\](\w+)[-\.,\\](\w+)[-\.,\\](\w+)'
pattern4 = r'(\w+)[-\.,\\](\w+)[-\.,\\](\w+)[-\.,\\](\w+)[-\.,\\](\w+)'

#Тут нужно будет вставить скомпилированые регулярки для многократного использования compile()
# reobj = re.compile("\b(\w+)[-\.,\\](\w+)\b")
obj = re.compile(r'[-\.,\\/_()#]')

#Открытие excel 1
bookone = openpyxl.open(r"/home/bender/Документы/rabs/fortest1.xlsx", read_only=True)
sheetone = bookone.active

#Открытие excel 2
booktwo = openpyxl.open(r"/home/bender/Документы/rabs/fortest2.xlsx", read_only=True)
sheettwo = booktwo.active

#Обработчик строк, разбивает строку по скомпиленой регулярке
def funk(stroka):
    if res := obj.split(stroka):
        return res
    else:
        return None

#Обработчик строк, возвращает словари
def kroba(stroka):
    if match := re.fullmatch(pattern1, stroka):
        raz, dva = match[1], match[2]
        #print('raz:', raz, 'dva:', dva)
        return {"raz" : raz, "dva" : dva}
    elif match := re.fullmatch(pattern2, stroka):
        raz, dva, tri = match[1], match[2], match[3]
        #print('raz:', raz, 'dva:', dva, 'tri:', tri)
        return {"raz" : raz, "dva" : dva, "tri" : tri}
    elif match := re.fullmatch(pattern3, stroka):
        raz, dva, tri, chetire, = match[1], match[2], match[3], match[4]
        #print('raz:', raz, 'dva:', dva, 'tri:', tri, 'chetire:', chetire)
        return {"raz" : raz, "dva" : dva, "tri" : tri, "chetire" : chetire}
    elif match := re.fullmatch(pattern4, stroka):
        raz, dva, tri, chetire, pat = match[1], match[2], match[3], match[4], match[5]
        #print('raz:', raz, 'dva:', dva, 'tri:', tri, 'chetire:', chetire, 'pat:', pat)
        return {"raz" : raz, "dva" : dva, "tri" : tri, "chetire": chetire, "pat" : pat}
    else:
        #print(stroka, 'neverniy')
        return None

#Дальше идет заполнение списка, в дальнейшем сделаю одной функцией, на входе будет поступать sheetnumber(one or two), Data(input or store)
#В последней строке для заполнения id используется функции: kroba(более точное сравнение по патернам) или funk(тупа сплитую строку)
#Запись элементов из excel в список1
for i, row in enumerate(range(1, sheetone.max_row+1)):
    kod = sheetone[row][0].value
    name = sheetone[row][1].value
    inputData.append({"name": name, "id": funk(kod)})

#Запись элементов из excel в список2
for i, row in enumerate(range(1, sheettwo.max_row+1)):
    kod = sheettwo[row][0].value
    name = sheettwo[row][1].value
    storeData.append({"name": name, "id": funk(kod)})

#тестил сравнение левенштайна
#https://habr.com/ru/post/491448/
#В статье на хабре показывают как сравнивать списки, думаю что это похоже на мой случай
a = fuzz.ratio('Блок цилиндров ЯМЗ-236М2 Н/О (под гильзу с поршнем 236-1004005-Б) АВТОДИЗЕЛЬ №','Блок цилиндров ЯМЗ-236НЕ2,БЕ2,6562 общ.ГБЦ под кор.гильзу Евро-2,3 АВТОДИЗЕЛЬ №')
b = fuzz.ratio('Блок цилиндров ЯМЗ-236М2 Н/О (под гильзу с поршнем 236-1004005-Б) АВТОДИЗЕЛЬ №','Блок цилиндров ЯМЗ-236М2 Н/О (под гильзу с поршнем 236-1004016-Б) АВТОДИЗЕЛЬ №')
#print(a,b)

#Пробовал ходить по спискам через циклы(старая версия), более новую не сохранил
# for it in range(len(inputData)):
#     chk=inputData[it]
#     tsk=chk.get('id')
#     dsk=tsk.get('model')
#
#     for ip in range(len(storeData)):
#         kones = range(len(storeData))
#         tgk=storeData[ip]
#         thk=tgk.get('id')
#         tlk=thk.get('model')
#         if dsk == tlk:
#             print(dsk, tlk, 'sucess')
#             break

#Выводы для тестов
#troka = input('Dai teksta\n')
#troka = inputData[1]
#print(troka)
#print(inputData)
#print(storeData)

# for k in range(len(inputText)):
#     print(inputText[k])
#
# for j in range(len(storeText)):
#     print(storeText[j])
