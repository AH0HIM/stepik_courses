"""
Таблица-1

Дано натуральное число (n≤ 9). Напишите программу, которая печатает таблицу размером n×3 состоящую из
данного числа (числа отделены одним пробелом).

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести таблицу размером n×3 состоящую из данного числа.

Примечание. В конце строки может быть пробел.

https://stepik.org/lesson/298795/step/5?unit=280622
"""

n = int(input())
for _ in range(n):
    for _ in range(3):
        print(n, end=' ')
    print()