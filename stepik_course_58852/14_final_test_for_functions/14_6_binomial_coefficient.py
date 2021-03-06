"""
Биномиальный коэффициент 🌶️
Напишите функцию compute_binom (n, k), которая принимает в качестве аргументов два натуральных числа n и k и возвращает
значение биномиального коэффициента, равного k!(n−k)!.

Примечание 1. Факториалом натурального числа nn, называется произведение всех натуральных чисел от 11 до nn, то есть
n!=1⋅2⋅3⋅…⋅n

Примечание 2. Реализуйте вспомогательную функцию factorial(n), вычисляющую факториал числа или воспользуйтесь уже
готовой функцией из модуля math.

https://stepik.org/lesson/334152/step/5?unit=317561
"""
from math import factorial


def compute_binom(n, k):
    return factorial(n) // (factorial(k) * factorial((n - k)))


n = int(input())
k = int(input())

print(compute_binom(n, k))
