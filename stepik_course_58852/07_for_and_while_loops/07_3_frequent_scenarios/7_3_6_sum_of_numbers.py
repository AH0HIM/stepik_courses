"""
Сумма чисел
На вход программе подается натуральное число n, а затем nn целых чисел, каждое на отдельной строке. Напишите программу,
которая подсчитывает сумму введенных чисел.

Формат входных данных
На вход программе подаются натуральное число n, а затем nn целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести сумму данных чисел.

https://stepik.org/lesson/294243/step/6?auth=login&unit=275922
"""

total = 0
for i in range(int(input())):
    total += int(input())
print(total)