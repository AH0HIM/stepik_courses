"""
2.6 Задачи по материалам недели 4 out of 5:
https://stepik.org/lesson/3369/step/10?unit=952
"""

a = [[int(i) for i in input().split()]]
b = input()
while b != 'end':
    a.append([int(i) for i in b.split()])
    b = input()
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i - 1][j] + a[i - len(a) + 1][j] + a[i][j - 1] + a[i][j - len(a[i]) + 1], end=' ')
    print()

