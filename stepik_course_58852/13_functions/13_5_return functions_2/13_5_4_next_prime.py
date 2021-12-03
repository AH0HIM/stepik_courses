"""
Next Prime 🌶️🌶️
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число большее числа num.

Примечание 1. Используйте функцию is_prime() из предыдущей задачи.

Примечание 2. Следующий программный код:

print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))

должен выводить:
7
11
17


https://stepik.org/lesson/334150/step/4?unit=317559
"""


def is_prime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


def get_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num


n = int(input())

print(get_next_prime(n))