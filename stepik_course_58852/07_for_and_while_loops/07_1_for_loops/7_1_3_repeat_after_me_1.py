"""
Повторяй за мной 1

Дано предложение и количество раз которое его надо повторить. Напишите программу, которая повторяет данное предложение
нужное количество раз.

Формат входных данных
В первой строке записано текстовое предложение, во второй — количество повторений.

Формат выходных данных
Программа должна вывести указанное текстовое предложение нужное количество раз. Каждое повторение должно начинаться с
новой строки.

https://stepik.org/lesson/265118/step/3?unit=246067
"""
s, n = input(), int(input())

for _ in range(n):
    print(s)
