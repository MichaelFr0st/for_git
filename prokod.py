# csv - работа с .csv, re - регулярки, fuzzywuzzy - Расстояние Левенштейна
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from emoji import emojize
import csv
import re
import time

start_time = time.time()

# Пути к файла которые будем сравнивать
csv_path_one = "/home/username/Документы/rabs/spares.csv"
csv_path_two = "/home/username/Документы/rabs/fbr.csv"

#Создание пустых списков под заполнение данными из csv
inputData = []
storeData = []
resData = []
# Список патернов для регулярных выражений
pattern1 = r'\b(\w+)[-\.,\\](\w+)\b'
pattern2 = r'(\w+)[-\.,\\_](\w+)[-\.,\\_](\w+)'
pattern3 = r'(\w+)[-\.,\\](\w+)[-\.,\\](\w+)[-\.,\\](\w+)'
pattern4 = r'(\w+)[-\.,\\](\w+)[-\.,\\](\w+)[-\.,\\](\w+)[-\.,\\](\w+)'

# Тут нужно будет вставить скомпилированые регулярки для многократного использования compile()
# reobj = re.compile("\b(\w+)[-\.,\\](\w+)\b")
obj = re.compile(r'[-\.,\\/_()#]')

#Обработчик строк, разбивает строку по скомпиленой регулярке
def funk(stroka):
    if res := obj.split(str(stroka)):
        return res
    else:
        print('to4no neverniy')
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
        print(stroka, 'neverniy')
        return None

# Функция формирования словарей и добавления их в список типа: [{'id':id,'name':name},{'id':id,'name':name}]
def csv_dict_reader(file_obj,dict_num):
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        razbiv = funk(line["id"])
        dict_num.append({"id":razbiv, "name":line["name"]})
#        print(line)
#        print(line["id"]), print(line["name"])

def csv_writer(data, path):
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)



# Начало, вызов заполнятора списков
with open(csv_path_one, "r") as i_obj:
    csv_dict_reader(i_obj,inputData)
with open(csv_path_two, "r") as s_obj:
    csv_dict_reader(s_obj,storeData)

#Логика сравнения:
# 1-ое сравнение In[id]:Ex[id]
# 2-ое сравнение In[id]:Ex[name]
# 3-е сравнение In[name]:Ex[name]
# 4-е сравнение In[kolvo]:Ex[kolvo]

#Сравнение списков и построчная запись в финальный csv файл
nomer = 0
a = len(storeData)
print(a)
for it in inputData:
    i = 0
    #nomer += 1
    for ik in storeData:
        if it['id'] != ik['id']:
            i +=1
            if i == a:
                #print(i)
                #print(it['id'], 'ne sovpalo')
                break
            else:
            #print(i)
                continue
        else:
            if it['id'] == ik['id']:
                print('\n',it['id'], it['name'], ik['id'], ik['name'], 'sovpalo')
    #print(nomer)


print("--- %s seconds ---" % (time.time() - start_time))
