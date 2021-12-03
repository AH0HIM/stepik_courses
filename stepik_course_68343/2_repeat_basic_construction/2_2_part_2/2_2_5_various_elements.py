﻿"""
Различные элементы

На вход программе подается строка текста, содержащая натуральные числа, расположенные по не убыванию. Из строки
формируется список чисел. Напишите программу для подсчета количества разных элементов в списке.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела, расположенные по
не убыванию.

Формат выходных данных
Программа должна вывести одно число – количество различных элементов списка.

Примечание. Задачу можно решить без множеств.

https://stepik.org/lesson/415554/step/5?unit=405083
"""
num = [int(i) for i in input().split()]

count = 1

for i in range(len(num) - 1):
    if num[i] != num[i + 1]:
        count += 1
print(count)
