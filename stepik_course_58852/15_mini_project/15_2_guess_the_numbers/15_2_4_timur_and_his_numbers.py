"""
Тимур и его числа
Тимур загадал число от 11 до nn. За какое наименьшее количество вопросов (на которые Тимур отвечает "больше"
или "меньше") Руслан может гарантированно угадать число Тимура?

Формат входных данных
На вход программе подается натуральное число nn.

Формат выходных данных
Программа должна вывести наименьшее количество вопросов, которых гарантированно хватит Руслану,
чтобы угадать число Тимура.
https://stepik.org/lesson/349845/step/4?unit=333700
"""

number = int(input())
count = 0

while number != 1:
    if number % 2 == 0:
        number = number // 2
        count += 1
    else:
        number = number // 2 + 1
        count += 1

print(count)


