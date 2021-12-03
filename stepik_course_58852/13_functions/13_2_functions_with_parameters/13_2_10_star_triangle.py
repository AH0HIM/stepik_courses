"""
Звездный треугольник
Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

fill – символ заполнитель;
base – величина основания равнобедренного треугольника;
а затем выводит его.

Примечание. Гарантируется, что основание треугольника – нечетное число.

https://stepik.org/lesson/333525/step/8?unit=316953
"""


def draw_triangle(fill, base):
    for i in range(base + 1):
        for j in range(i):
            if i + j <= base:
                print(fill, end='')
        print()


fill = input()
base = int(input())

draw_triangle(fill, base)
