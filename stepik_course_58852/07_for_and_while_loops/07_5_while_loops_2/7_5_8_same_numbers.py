"""
Одинаковые цифры
Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести «YES» если число состоит из одинаковых цифр и «NO» в противном случае.

https://stepik.org/lesson/265122/step/9?auth=login&unit=246071
"""

n = int(input())
last_digit = n % 10
flag = True
while n > 0:
    second_digit = n % 10
    if last_digit != second_digit:
        flag = False
    n //= 10
if flag:
    print('YES')
else:
    print('NO')