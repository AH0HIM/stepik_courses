"""
Звездная рамка
На вход программе подается натуральное число n. Напишите программу, которая печатает звездную рамку размерами n×19.

Формат входных данных
На вход программе подаётся натуральное число n∈[3;19] — высота звездной рамки.

Формат выходных данных
Программа должна вывести звездную рамку размерами n×19.

Подсказка. Для печати звездной линии используйте умножение строки на число.

https://stepik.org/lesson/294080/step/4?unit=275759
"""

n = int(input())
print('*' * 19)
for i in range(n-2):
    print('*' + ' ' * 17 + '*')
print('*' * 19)