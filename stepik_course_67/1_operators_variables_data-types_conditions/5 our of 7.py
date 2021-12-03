"""
1.12 Задачи по материалам недели 5 our of 7 steps:
https://stepik.org/lesson/5047/step/5?unit=1086
"""

a, b, c = int(input()), int(input()), int(input())

if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b > c:
    b, c = c, b

print(a)
print(b)
print(c)
