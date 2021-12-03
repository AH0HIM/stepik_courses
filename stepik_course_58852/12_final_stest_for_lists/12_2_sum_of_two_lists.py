"""
Сумма двух списков
На вход программе подаются две строки текста, содержащие целые числа. Из данных строк формируются списки чисел L и M. Напишите программу, которая создает третий список, элементами которого являются суммы соответствующих элементов списков L и M. Далее программа должна вывести каждый элемент полученного списка на одной строке через 1 пробел.

Формат входных данных
На вход программе подаются две строки текста, содержащие целые числа, разделенные символом пробела.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Количество чисел в обеих строках одинаковое.

https://stepik.org/lesson/327221/step/2?unit=310520
"""

l, m = input().split(), input().split()
print(*(int(l[i]) + int(m[i]) for i in range(len(l))))

