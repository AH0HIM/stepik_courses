"""
Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево, к тому же ведьмак
не принимает купюры, он принимает только чеканные монеты. В мире ведьмака существуют монеты с номиналами 1, \, 5, \, 10, \, 251,5,10,25.

Напишите программу, которая определяет какое минимальное количество чеканных монет нужно заплатить ведьмаку.

Формат входных данных
На вход программе подается одно натуральное число, цена за услугу ведьмака.

Формат выходных данных
Программа должна вывести минимально возможное количество чеканных монет для оплаты.

https://stepik.org/lesson/265121/step/14?unit=246070
"""
n = int(input())
counter = 0
while n >= 25:
    counter += 1
    n -= 25
while 25 > n >= 10:
    counter += 1
    n -= 10
while 10 > n >= 5:
    counter += 1
    n -= 5
while 5 > n >= 1:
    counter += 1
    n -= 1
print(counter)