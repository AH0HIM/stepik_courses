"""
Сумма цифр
Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.

https://stepik.org/lesson/333525/step/10?unit=316953
"""


def print_digit_sum(num):
    print(sum(int(i) for i in str(num)))


n = int(input())

print_digit_sum(n)
