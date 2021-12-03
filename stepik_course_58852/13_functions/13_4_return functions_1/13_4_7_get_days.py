"""
Количество дней
Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.

Примечание 1. Гарантируется, что передаваемый аргумент находится в диапазоне от 1 до 12.

Примечание 2. Считайте, что год является невисокосным.

Примечание 3. Следующий программный код:
print(get_days(1))
print(get_days(2))
print(get_days(9))

должен выводить:
31
28
30

https://stepik.org/lesson/331754/step/7?unit=315133
"""


def get_days(month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        return 28


num = int(input())

print(get_days(num))