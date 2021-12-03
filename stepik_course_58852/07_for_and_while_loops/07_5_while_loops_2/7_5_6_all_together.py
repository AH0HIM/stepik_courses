"""
Все вместе
Дано натуральное число. Напишите программу, которая вычисляет:
- сумму его цифр;
- количество цифр в нем;
- произведение его цифр;
- среднее арифметическое его цифр;
- его первую цифру;
- сумму его первой и последней цифры.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке.

https://stepik.org/lesson/265122/step/7?auth=login&unit=246071
"""
n = int(input())
total_sum, counter, total_comp, arithmetic, first_digit = 0, 0, 1, 0, 0
last_digit = n % 10
while n != 0:
    total_sum += n % 10
    counter += 1
    total_comp *= n % 10
    arithmetic = total_sum / counter
    first_digit = n
    n = n // 10
print(total_sum, counter, total_comp, arithmetic, first_digit, first_digit+last_digit, sep='\n')
