"""
Дополните приведенный код, так чтобы он вывел сумму квадратов элементов списка numbers.

https://stepik.org/lesson/328948/step/2?unit=312239
"""

numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
s = []

for num in numbers:
    s.append(num ** 2)

print(sum(s))