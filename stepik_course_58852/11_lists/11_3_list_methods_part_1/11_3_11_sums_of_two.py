"""
Суммы двух
На вход программе подается натуральное число n≥2, а затем nn целых чисел. Напишите программу, которая создает из
указанных чисел список, состоящий из сумм соседних чисел (0 и 1,1 и 2,2 и 3 и т.д.).

Формат входных данных
На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести список, состоящий из сумм соседних чисел.

https://stepik.org/lesson/327207/step/11?unit=310501
"""

n, a = int(input()), int(input())

lst = []

for _ in range(n - 1):
    b = int(input())
    lst.append(a + b)
    a = b
print(lst)