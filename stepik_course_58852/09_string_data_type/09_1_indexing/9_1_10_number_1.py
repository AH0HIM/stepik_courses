"""
Цифра 1
На вход программе подается одна строка состоящая из цифр. Напишите программу, которая считает сумму цифр данной строки.

Формат входных данных
На вход программе подается одна строка состоящая из цифр.

Формат выходных данных
Программа должна вывести сумму цифр данной строки.

https://stepik.org/lesson/284101/step/10?unit=265440
"""
s = input()
total = 0

for i in s:
     total += int(i)
print(total)
