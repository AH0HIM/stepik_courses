"""
Все вместе 2
Дано натуральное число. Напишите программу, которая вычисляет:
- количество цифр 3 в нем;
- сколько раз в нем встречается последняя цифра;
- количество четных цифр;
- сумму его цифр, больших пяти;
- произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
- сколько раз в нем встречается цифры 0 и 5 (всего суммарно).

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке.

https://stepik.org/lesson/294080/step/6?unit=275759
"""
n = int(input())
last_digit = n % 10

counter_three = 0
counter_last_digit = 0


even_number = 0
counter_five = 0
counter_seven = 1
counter_five_seven = 0
while n != 0:
    a = n % 10
    if a == 3:
        counter_three += 1
    if a == last_digit:
        counter_last_digit += 1
    if a % 2 == 0:
        even_number += 1
    if a > 5:
        counter_five += a
    if a > 7:
        counter_seven *= a
    if a in (0, 5):
        counter_five_seven += 1
    n //= 10

print(counter_three)
print(counter_last_digit)
print(even_number)
print(counter_five)
print(counter_seven)
print(counter_five_seven)