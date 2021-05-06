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

#Открытие excel 1
bookone = openpyxl.open(r".\fortest1.xlsx", read_only=True)
sheetone = bookone.active

#Открытие excel 2
booktwo = openpyxl.open(r".\fortest2.xlsx", read_only=True)
sheettwo = booktwo.active

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

#Запись элементов из excel в список1
for i, row in enumerate(range(1, sheetone.max_row+1)):
    kod = sheetone[row][0].value
    name = sheetone[row][1].value
    inputData.append({"name": name, "id": kroba(kod)})

#Запись элементов из excel в список2
for i, row in enumerate(range(1, sheettwo.max_row+1)):
    kod = sheettwo[row][0].value
    name = sheettwo[row][1].value
    storeData.append({"name": name, "id": kroba(kod)})



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



#troka = input('Dai teksta\n')

#print(inputData)
#print(storeData)

