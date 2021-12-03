"""
2.6 Задачи по материалам недели:
https://stepik.org/lesson/3369/step/7?unit=952
"""

a = int(input())
c = a ** 2

while a != 0:
    b = int(input())
    a += b
    c += b ** 2
print(c)