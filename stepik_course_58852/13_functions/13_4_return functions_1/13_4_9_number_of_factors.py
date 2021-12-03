"""
Делители 2
Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество делителей данного числа.

Примечание 1. Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.

Примечание 2. Следующий программный код:
print(number_of_factors(1))
print(number_of_factors(5))
print(number_of_factors(10))

должен выводить:
1
2
4

https://stepik.org/lesson/331754/step/7?unit=315133
"""


def number_of_factors(num):
    return len([i for i in range(1, num + 1) if n % i == 0])


n = int(input())
print(number_of_factors(n))