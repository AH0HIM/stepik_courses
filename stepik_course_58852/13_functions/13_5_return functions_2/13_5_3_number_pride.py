"""
Is a Number Prime? 🌶️
Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True если число является простым и False в противном случае.

Примечание. Следующий программный код:
print(is_prime(1))
print(is_prime(10))
print(is_prime(17))

должен выводить:
False
False
True


https://stepik.org/lesson/334150/step/3?unit=317559
"""


def is_prime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


n = 101
print(is_prime(n))
