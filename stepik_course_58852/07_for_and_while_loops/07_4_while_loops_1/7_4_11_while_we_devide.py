"""
Пока делимся
На вход программе подается последовательность целых чисел делящихся на 77, каждое число на отдельной строке. Концом
последовательности является любое число не делящееся на 77. Напишите программу, которая выводит члены данной
последовательности.

Формат входных данных
На вход программе подается последовательность чисел, каждое число на отдельной строке.

Формат выходных данных
Программа должна вывести члены данной последовательности.

https://stepik.org/lesson/265121/step/11?unit=246070
"""
n = int(input())
while n % 7 == 0:
    print(n)
    n = int(input())
