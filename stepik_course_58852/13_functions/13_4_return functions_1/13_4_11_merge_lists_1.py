"""
Merge lists 1
Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных по возрастанию списка, состоящих из целых чисел, и объединяет их в один отсортированный список.

Примечание 1. Списки list1 и list2 могут иметь разную длину.

Примечание 2. Можно использовать списочный метод sort(), а можно обойтись и без него 😎.

Примечание 3. Следующий программный код:

print(merge([1, 2, 3], [5, 6, 7, 8]))
print(merge([1, 7, 10, 16], [5, 6, 13, 20]))
должен выводить:

[1, 2, 3, 5, 6, 7, 8]
[1, 5, 6, 7, 10, 13, 16, 20]

https://stepik.org/lesson/331754/step/11?unit=315133
"""


def merge(list1, list2):
    result = list1 + list2
    result.sort()
    return result


numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))
