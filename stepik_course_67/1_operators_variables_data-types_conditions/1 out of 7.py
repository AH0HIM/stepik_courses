"""
1.12 Задачи по материалам недели 1 our of 7 steps:
https://stepik.org/lesson/5047/step/1?unit=1086
"""

a = int(input())
b = int(input())
c = int(input())
s = (a + b + c) / 2

print((s * (s - a) * (s - b) * (s - c)) ** 0.5)
