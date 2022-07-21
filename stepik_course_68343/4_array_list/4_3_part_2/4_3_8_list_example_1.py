"""
Список по образцу 1
На вход программе подается число n. Напишите программу, которая создает и выводит построчно список, состоящий из n
списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].

Формат входных данных
На вход программе подается натуральное число n.

Формат выходных данных
Программа должна вывести построчно указанный список.

https://stepik.org/lesson/416753/step/8?unit=406261
"""
import timeit
timeit.timeit(stmt='''\

num = 5

result = []

for _ in range(num):
    result.append(list(range(1, num + 1)))''', number=5)
print(timeit.timeit())

timeit.timeit(stmt='''\
num = 5
list1 = [[j for j in range(1, num + 1)] for i in range(1, num + 1)]''', number=5)

print(timeit.timeit())
