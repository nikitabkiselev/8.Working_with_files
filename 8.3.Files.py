#Определение функции-компаратора
def comparator(doc):
    return len(doc)

files = []
list_files = ('1.txt', '2.txt', '3.txt')

#Добавление в исходные файлы строк Название и Количество строк
for file_name in list_files:
     with open(file_name, 'r', encoding='UTF-8') as fr:
          lines_number = fr.readlines()
     with open(file_name, 'r', encoding='UTF-8') as fr:
          text = fr.read()
     with open(file_name, 'w', encoding='UTF-8') as fw:
          print(file_name, len(lines_number), text, sep='\n', file=fw)

#Сортировка файлов в списке по возрастанию количества строк
for file_name in list_files:
     with open(file_name, 'r', encoding='UTF-8') as fr:
         files.append(fr.readlines())
files.sort(key=comparator)

#Запись в новый файл
with open('new_file.txt', 'w', encoding='UTF-8') as fw:
    for file in files:
         fw.writelines(file)
#         f.write('\n')

#Приведение исходных файлов в исходное состояние
for file_name in list_files:
     with open(file_name, 'r', encoding='UTF-8') as fr:
          lines = fr.readlines()
     del (lines[0], lines[0])
     lines[-1] = lines[-1].rstrip('\n')
     with open(file_name, 'w', encoding='UTF-8') as fr:
          fr.writelines(lines)
