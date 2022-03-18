"""
Merge lists 2
На вход программе подается число n, а затем n строк, содержащих целые числа в порядке возрастания. Из данных строк
формируются списки чисел. Напишите программу, которая объединяет указанные списки в один отсортированный список с
помощью функции quick_merge(), а затем выводит его.

Формат входных данных
На вход программе подается натуральное число n, а затем n строк, содержащих целые числа в порядке возрастания,
разделенные символом пробела.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

https://stepik.org/lesson/331754/step/13?unit=315133
"""


def quick_merge(list1, list2):
    result = []

    p1 = 0
    p2 = 0

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result


n = int(input())
list1 = [int(i) for i in input().split()]

total = []

for i in range(1, n):
    list2 = [int(i) for i in input().split()]
    list3 = quick_merge(list1, list2)
    list1 = list3

print(list1)
