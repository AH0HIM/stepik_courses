"""
умма чисел
На вход программе подается натуральное число nn. Напишите программу, которая подсчитывает сумму тех чисел от 1 до n
(включительно) квадрат которых оканчивается на 2, 5 или 8.

Формат входных данных
На вход программе подается натуральное число nn.

Формат выходных данных
Программа должна вывести единственное число в соответствии с условием задачи.

Примечание. Если таких чисел нет в указанном диапазоне, то следует вывести 0.

https://stepik.org/lesson/294243/step/8?auth=login&unit=275922
"""
total = 0
for i in range(1, int(input())+1):
    if i % 10 == 5:
        total += i
print(total)
