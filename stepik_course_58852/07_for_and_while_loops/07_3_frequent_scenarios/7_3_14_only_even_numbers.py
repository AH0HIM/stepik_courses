"""
Only even numbers 🌶️
Напишите программу, которая считывает последовательность из 10 целых чисел и определяет является ли каждое из них четным или нет.

Формат входных данных
На вход программе подаются 10 целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести строку «YES», если все числа четные и «NO» в ином случае.

https://stepik.org/lesson/294243/step/14?auth=login&unit=275922
"""
flag = True

for _ in range(10):
    if int(input()) % 2 != 0:
        flag = False
if flag is True:
    print('YES')
else:
    print('NO')