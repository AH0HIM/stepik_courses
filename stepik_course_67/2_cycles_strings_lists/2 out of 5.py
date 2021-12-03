"""
2.6 Задачи по материалам недели 2 out of 5:
https://stepik.org/lesson/3369/step/8?unit=952
"""

a = int(input())
b = []
s = len(b)
i = 0
j = 0
while i < a:
    i += 1
    while i > j:
        b.append(i)
        j += 1
        if len(b) == a:
            break
    j = 0
    if len(b) == a:
        break
print(*b)

