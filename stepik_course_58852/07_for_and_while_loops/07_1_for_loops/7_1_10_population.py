"""
Популяция
На вход программе подается три натуральных числа m, p, n:

m:m: стартовое количество организмов;
p:p: среднесуточное увеличение в %;
n:n: количество дней для размножения.
Напишите программу, которая предсказывает размер популяции организмов. Программа должна выводить размер популяции
в каждый день, начиная с 11 и заканчивая nn-м днем.

Формат входных данных
На вход программе подается три натуральных числа.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

https://stepik.org/lesson/265118/step/10?unit=246067
"""

m, p, n = int(input()), int(input()), int(input())

for i in range(n):
    print(i + 1, (m * (p / 100 + 1) ** i))
