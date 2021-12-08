"""
Факториал
На вход программе подается натуральное число nn. Напишите программу, которая вычисляет n!.

Входные данные
На вход программе подается натуральное число (n≤12).

Выходные данные
Программа должна вывести единственное число в соответствии с условием задачи.

Примечание. Факториалом натурального числа nn, называется произведение всех натуральных чисел от 11 до n, то есть
n!=1⋅2⋅3⋅…⋅n

https://stepik.org/lesson/294243/step/9?auth=login&unit=275922
"""

n = int(input())

total = 1
for i in range(1, n + 1):
    total = total * i
print(total)