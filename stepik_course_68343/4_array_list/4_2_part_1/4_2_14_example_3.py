"""
Дополните приведенный код, используя цикл for и встроенную функцию max(), чтобы он выводил один общий максимальный
элемент среди всех элементов вложенных списков list1.

https://stepik.org/lesson/416752/step/14?unit=406260
"""
list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

maximum = -1

for li in list1:
    if max(li) > maximum:
        maximum = max(li)

print(maximum)
