"""
Вторая цифра
Дано натуральное число (n>9). Напишите программу, которая определяет его вторую (с начала) цифру.

Формат входных данных
На вход программе подается одно натуральное число, состоящее как минимум из двух цифр.

Формат выходных данных
Программа должна вывести его вторую (с начала) цифру.

https://stepik.org/lesson/265122/step/8?auth=login&unit=246071
"""
n = int(input())
while n > 99:
    n //= 10
print(n % 10)
