"""
Упаковка дубликатов 🌶️

На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает последовательности
одинаковых символов заданной строки в подсписки.

Формат входных данных
На вход программе подается строка текста, содержащая символы, отделенные символом пробела.

Формат выходных данных
Программа должна вывести указанный вложенный список.

https://stepik.org/lesson/416753/step/12?unit=406261
"""

my_list = []

for item in input().split():
    my_list.append([item]) if not my_list or item not in my_list[-1] else my_list[-1].append(item)
print(my_list)


'''
res = []
a = str(input()).split()
for i in a:
    if len(res) == 0 or i not in res[-1]:
        res.append([i])
    else:
        res[-1].append(i)
print(res)
'''