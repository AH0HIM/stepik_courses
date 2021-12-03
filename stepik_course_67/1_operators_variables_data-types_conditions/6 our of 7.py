"""
1.12 Задачи по материалам недели 6 our of 7 steps:
https://stepik.org/lesson/5047/step/6?unit=1086
"""
n = int(input())

if n % 10 == 1 and n % 100 != 11:
    print(n, 'программист')
elif 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
    print(n, 'программиста')
else:
    print(n, 'программистов')