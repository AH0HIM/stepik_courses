"""
1.12 Задачи по материалам недели 7 our of 7 steps:
https://stepik.org/lesson/5047/step/7?unit=1086
"""
a, b, c, d, e, f = input()

if int(a) + int(b) + int(c) == int(d) + int(e) + int(f):
    print('Счастливый')
else:
    print('Обычный')