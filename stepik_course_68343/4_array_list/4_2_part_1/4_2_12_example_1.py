"""
Дополните приведенный код, используя списочный метод append(), чтобы список list1 имел вид:

list1 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

https://stepik.org/lesson/416752/step/12?unit=406260
"""


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)

print(list1)
