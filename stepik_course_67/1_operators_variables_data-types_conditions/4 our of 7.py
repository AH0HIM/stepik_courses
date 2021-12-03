"""
1.12 Задачи по материалам недели 4 our of 7 steps:
https://stepik.org/lesson/5047/step/4?unit=1086
"""
str = str(input())

if str == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    s = (a + b + c) / 2
    print(float((s * (s - a) * (s - b) * (s - c)) ** 0.5))
elif str == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(float(a * b))
elif str == 'круг':
    r = int(input())
    print(float(3.14 * (r ** 2)))