"""
Сумма чисел
На вход программе подается последовательность целых чисел, каждое число на отдельной строке. Концом последовательности
является любое отрицательное число. Напишите программу, которая выводит сумму всех членов данной последовательности.

Формат входных данных
На вход программе подается последовательность чисел, каждое число на отдельной строке.

Формат выходных данных
Программа должна вывести сумму членов данной последовательности.

https://stepik.org/lesson/265121/step/12?unit=246070
"""

n, total = int(input()), 0
while n >= 0:
    total += n
    n = int(input())
print(total)