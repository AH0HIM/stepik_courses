"""
Переворот числа

Дано пятизначное или шестизначное натуральное число. Напишите программу, которая изменит порядок его последних
пяти цифр на обратный.

Формат входных данных
На вход программе подается одно натуральное пятизначное или шестизначное число.

Формат выходных данных
Программа должна вывести число, которое получится в результате разворота, указанного в условии задачи.
Число нужно выводить без незначащих нулей.

https://stepik.org/lesson/415553/step/7?unit=405082
"""

num = input()
if len(num) == 5:
    print(int(num[::-1]))
else:
    print(int(num[0] + (num[:-6:-1])))
