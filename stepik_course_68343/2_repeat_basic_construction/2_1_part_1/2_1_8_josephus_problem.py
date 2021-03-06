"""
Задача Иосифа Флавия 🌶️🌶️

nn человек, пронумерованных числами от 1 до n, стоят в кругу. Они начинают считаться, каждый kk-й по счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека. Напишите программу, определяющую номер человека, который останется в кругу последним.

Формат входных данных
На вход программе подаются два числа nn и k, записанные на отдельных строках.

Формат выходных данных
Программа должна вывести одно число – номер человека, который останется в кругу последним.

Примечание 1. Подробнее ознакомиться с классической задачей Иосифа Флавия можно тут.

Примечание 2. Визуализацию работы алгоритма можно посмотреть тут.

https://stepik.org/lesson/415553/step/10?unit=405082
"""

n, k = int(input()), int(input())

res = 0

for i in range(1, n + 1):
    res = (res + k) % i
print(res + 1)
