"""
Количество цифр
На вход программе подается строка текста. Напишите программу, которая подсчитывает количество цифр в данной строке.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести количество цифр в данной строке.

https://stepik.org/lesson/303083/step/11?unit=284990
"""

s = input()
count = 0

for i in s:
    if '0' <= i <= '9':
        count += 1
print(count)