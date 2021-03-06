"""
Знакочередующаяся сумма
На вход программе подается натуральное число n. Напишите программу вычисления знакочередующей суммы
1-2+3-4+5-6 + (-1)n+1n.

Входные данные
На вход программе подается натуральное число n.

Выходные данные
Программа должна вывести единственное число в соответствии с условием задачи.

https://stepik.org/lesson/294243/step/12?auth=login&unit=275922
"""

n = int(input())

counter = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        counter += (- i)
    else:
        counter += i
print(counter)