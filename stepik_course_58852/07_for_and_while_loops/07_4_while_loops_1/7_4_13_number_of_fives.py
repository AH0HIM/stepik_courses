"""
Количество пятерок
На вход программе подается последовательность целых чисел от 11 до 55, характеризующее оценку ученика, каждое число на отдельной строке. Концом последовательности является любое отрицательное число, либо число большее 55. Напишите программу, которая выводит количество пятерок.

Формат входных данных
На вход программе подается последовательность чисел, каждое число на отдельной строке.

Формат выходных данных
Программа должна вывести количество пятерок.

https://stepik.org/lesson/265121/step/13?unit=246070
"""
n, total = int(input()), 0
while 0 <= n <= 5:
    if n == 5:
        total += 1
    n = int(input())
print(total)