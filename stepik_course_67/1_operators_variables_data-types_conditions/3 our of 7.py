"""
1.12 Задачи по материалам недели 3 our of 7 steps:
https://stepik.org/lesson/5047/step/3?unit=1086
"""

a = float(input())
b = float(input())
c = str(input())

if c == 'mod' and b != 0.0:
    print(a % b)
elif c == 'pow':
    print(a ** b)
elif c == 'div' and b != 0.0:
    print(a // b)
elif c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '/' and b != 0.0:
    print(a / b)
elif c == '*':
    print(a * b)
else:
    print('Деление на 0!')