# n = int(input())
# stars = '*'
# while len(stars) < n:
#     print(stars)
#     stars += '*'
#
# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1
#
#
# s = 0
# i = 3(
#
# while i <= 7:
#     s += i
#     i += 1
# print(s)
#
# s = int(input())
# i = 0
# while s != 0:
#     i += s
#     s = int(input())
# print(i)
#
#
# a, b = int(input()), int(input())
# i = 1
# while i % a != 0 or i % b != 0:
#     i += 1
# print(i)
#
# i = 0
# while i <= 100:
#     s = int(input())
#     if s < 10:
#         continue
#     if s > 100:
#         break
#     print(s)
#
# n = int(input())
#
# for i in range(n):
#     for j in range(n):
#         print('*' * n, end='')
#     print()
# #
#
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
#
# for i in range(c, d + 1):
#     print('\t', i, sep='', end='')
# print()
# for j in range(a, b + 1):
#     print(j, end='\t')
#     for h in range(c, d + 1):
#         print(j * h, end='\t')
#     print()
#
#
# a, b = input().split()
# a, b = int(a), int(b)
# s = 0
# for i in range(a, b + 1):
#     if i % 2 == 1:
#         s += i
# print(s)
#
# a, b = input().split()
# a, b = int(a), int(b)
# s = 0
# if a % 2 == 0:
#     a += 1
# for i in range(a, b + 1, 2):
#     s += i
# print(s)
#
# a, b = (int(i) for i in input().split())
# s = 0
#
# if a % 2 == 0:
#     a += 1
# for i in range(a, b + 1, 2)
#     s += i
# print(s)
#
# a, b = int(input()), int(input())
# s = 0
# h = 0
# if a % 3 == 1:
#     a += 2
#     for i in range(a, b + 1, 3):
#         s += i
#         h += 1
#     print(s/h)
# elif a % 3 == 2:
#     a += 1
#     for i in range(a, b + 1, 3):
#         s += i
#         h += 1
#     print(s/h)
# else:
#     for i in range(a, b + 1, 3):
#         s += i
#         h += 1
#     print(s/h)
#
#
# genome = input()
# cnt = 0
# for c in genome:
#     if c == 'C':
#         cnt += 1
# print(cnt)
#
# genome = input()
# print(genome.count('C'))
'''
Некоторые методы у строк:
s = 'aTGcc' p = 'cc'
- s.upper() - 'ATGCC' - все маленькие строчки на большие;
- s.lower() - 'atgcc' - все большие строчки на маленькие;
- s.count(c) - 2 - сколько раз встречается <c>;
- s.find(c) - 3 - найти первое вхождение;
- s.replace('c', 'C') - aTGCC - заменяет временно;

s = 'agTtcAGtc'
s.upper().count('gt'.upper())

результат: 2
'''
#
#
# s = input()
# g = s.upper().count('G'.upper())
# c = s.upper().count('C'.upper())
# # print(((g + c) / len(s)) * 100)
#
#
# a = 0
# s = input().lower()
# for i in range(len(s)):
#     if s[i] == 'c':
#         a += 1
# print(a)
#
# s = input()
# i = 0
# j = len(s) - 1
# is_palindrom = True
#
# while i < j:
#     if s[i] != s[j]:
#         is_palindrom = False
#     i += 1
#     j -= 1
# if is_palindrom:
#     print('YES')
# else:
#     print('NO')
# s = 'abcdefghijk'
# print(s[3:6])
# print(s[:6])
# print(s[3:])
# print(s[::-1])
# print(s[-3:])
# print(s[:-6])
# print(s[-1:-10:-2])

# s = input()
# n = len(s)
# count = 1
# for i in range(n - 1):
#     if s[i] == s[i+1]:
#         count += 1
#     else:
#         s[i] != s[i+1]
#         print(s[i], count, end='', sep='')
#         count = 1
# # print(s[-1], count, end='', sep='')
#
# a = [int(i) for i in input().split()]
# count = 0
# for i in a:
#     count += i
# print(count)
#
# a = [int(i) for i in input().split()]
# n = len(a)
# if n != 1:
#     for i in range(n - 1):
#         print(a[i-1] + a[i+1], end=' ')
#     print(a[-2] + a[0])
# else:
#     print(a[0])
#
# a = [int(i) for i in input().split()]
# b = []
# a.sort()
# n = len(a)
# if n != 1:
#     for i in range(n-1):
#         if a[i] == a[i+1] and a[i] not in b:
#             b.append(a[i])
# print(*b)

# Поле для игры Сапер
# rows, columns, mines = (int(i) for i in input().split())  # строки, столбцы, мины
# a = [[0 for j in range(columns)] for i in range(rows)]  # пустая таблица из 0
# for i in range(mines):  # перебираем количество мин
#     rw, cl = (int(i) -1 for i in input().split())  # записываем строку и столбец одной мины при каждом проходе
#     a[rw][cl] = - 1  # записываем минус по координатам
# for i in range(rows):  # поиск мин вокруг # перебираем строки
#     for j in range(columns):  # перебираем столбцы
#         if a[i][j] == 0:  # ячейка без мины
#             for di in range(-1, 2):  # перебираем соседные строки -1 0 1
#                 for dj in range(-1, 2):  # перебираем соседние столбцы -1 0 1
#                     ai = i + di  # кординат по строке
#                     aj = j + dj  # координат по столбцу
#                     if 0 <= ai < rows and 0 <= aj < columns and a[ai][aj] == -1:  # проверка вхождения в диапазон
#                         # и мины по соседству
#                         a[i][j] += 1
# for i in range(rows):
#     for j in range(columns):
#         if a[i][j] == -1:
#             print('*', end='')
#         elif a[i][j] == 0:
#             print('.', end='')
#         else:
#             print(a[i][j], end='')
#     print()
#
# Задачи по материалам недели 6 out of 11 steps
#
#
# a = int(input())
# total = 0
# total += a
# quad = 0
# while total != 0:
#     quad += total ** 2
#     print(quad)
#     a = int(input())
#     total += a
#     quad += total ** 2
# print(quad)
#
#
# a = int(input())
# c = a ** 2
#
# while a != 0:
#     b = int(input())
#     a += b
#     c += b ** 2
# print(c)
# Задачи по материалам недели 7 out of 11 steps

# a = int(input())
# b = []
# s = len(b)
# i = 0
# j = 0
# while i < a:
#     i += 1
#     while i > j:
#         b.append(i)
#         j += 1
#         if len(b) == a:
#             break
#     j = 0
#     if len(b) == a:
#         break
# print(*b)
#
# n = int(7)  # считываем
# i = 1
# count = 0
#
# while count < n:  # условие на превышение переборов
#     for j in range(i):
#         if count < n:
#             print(i, end='')
#             count += 1
#         else:
#             break
#     i += 1
#
#
# lst = [int(i) for i in input().split()]
# b = []
# x = int(input())
# n = len(lst)
#
#
# for i in range(n - 1):
#     if lst[i] == x:
#         b.append(i)
#     elif lst[i] == x:
#         continue
# print(b)
# n = int(input())
# stars = '*'
# while len(stars) < n:
#     print(stars)
#     stars += '*'
#
# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1
#
#
# s = 0
# i = 3(
#
# while i <= 7:
#     s += i
#     i += 1
# print(s)
#
# s = int(input())
# i = 0
# while s != 0:
#     i += s
#     s = int(input())
# print(i)
#
#
# a, b = int(input()), int(input())
# i = 1
# while i % a != 0 or i % b != 0:
#     i += 1
# print(i)
#
# i = 0
# while i <= 100:
#     s = int(input())
#     if s < 10:
#         continue
#     if s > 100:
#         break
#     print(s)
#
# n = int(input())
#
# for i in range(n):
#     for j in range(n):
#         print('*' * n, end='')
#     print()
# #
#
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
#
# for i in range(c, d + 1):
#     print('\t', i, sep='', end='')
# print()
# for j in range(a, b + 1):
#     print(j, end='\t')
#     for h in range(c, d + 1):
#         print(j * h, end='\t')
#     print()
#
#
# a, b = input().split()
# a, b = int(a), int(b)
# s = 0
# for i in range(a, b + 1):
#     if i % 2 == 1:
#         s += i
# print(s)
#
# a, b = input().split()
# a, b = int(a), int(b)
# s = 0
# if a % 2 == 0:
#     a += 1
# for i in range(a, b + 1, 2):
#     s += i
# print(s)
#
# a, b = (int(i) for i in input().split())
# s = 0
#
# if a % 2 == 0:
#     a += 1
# for i in range(a, b + 1, 2)
#     s += i
# print(s)
#
# a, b = int(input()), int(input())
# s = 0
# h = 0
# if a % 3 == 1:
#     a += 2
#     for i in range(a, b + 1, 3):
#         s += i
#         h += 1
#     print(s/h)
# elif a % 3 == 2:
#     a += 1
#     for i in range(a, b + 1, 3):
#         s += i
#         h += 1
#     print(s/h)
# else:
#     for i in range(a, b + 1, 3):
#         s += i
#         h += 1
#     print(s/h)
#
#
# genome = input()
# cnt = 0
# for c in genome:
#     if c == 'C':
#         cnt += 1
# print(cnt)
#
# genome = input()
# print(genome.count('C'))
'''
Некоторые методы у строк:
s = 'aTGcc' p = 'cc'
- s.upper() - 'ATGCC' - все маленькие строчки на большие;
- s.lower() - 'atgcc' - все большие строчки на маленькие;
- s.count(c) - 2 - сколько раз встречается <c>;
- s.find(c) - 3 - найти первое вхождение;
- s.replace('c', 'C') - aTGCC - заменяет временно;

s = 'agTtcAGtc'
s.upper().count('gt'.upper())

результат: 2
'''
#
#
# s = input()
# g = s.upper().count('G'.upper())
# c = s.upper().count('C'.upper())
# # print(((g + c) / len(s)) * 100)
#
#
# a = 0
# s = input().lower()
# for i in range(len(s)):
#     if s[i] == 'c':
#         a += 1
# print(a)
#
# s = input()
# i = 0
# j = len(s) - 1
# is_palindrom = True
#
# while i < j:
#     if s[i] != s[j]:
#         is_palindrom = False
#     i += 1
#     j -= 1
# if is_palindrom:
#     print('YES')
# else:
#     print('NO')
# s = 'abcdefghijk'
# print(s[3:6])
# print(s[:6])
# print(s[3:])
# print(s[::-1])
# print(s[-3:])
# print(s[:-6])
# print(s[-1:-10:-2])

# s = input()
# n = len(s)
# count = 1
# for i in range(n - 1):
#     if s[i] == s[i+1]:
#         count += 1
#     else:
#         s[i] != s[i+1]
#         print(s[i], count, end='', sep='')
#         count = 1
# # print(s[-1], count, end='', sep='')
#
# a = [int(i) for i in input().split()]
# count = 0
# for i in a:
#     count += i
# print(count)
#
# a = [int(i) for i in input().split()]
# n = len(a)
# if n != 1:
#     for i in range(n - 1):
#         print(a[i-1] + a[i+1], end=' ')
#     print(a[-2] + a[0])
# else:
#     print(a[0])
#
# a = [int(i) for i in input().split()]
# b = []
# a.sort()
# n = len(a)
# if n != 1:
#     for i in range(n-1):
#         if a[i] == a[i+1] and a[i] not in b:
#             b.append(a[i])
# print(*b)

# Поле для игры Сапер
# rows, columns, mines = (int(i) for i in input().split())  # строки, столбцы, мины
# a = [[0 for j in range(columns)] for i in range(rows)]  # пустая таблица из 0
# for i in range(mines):  # перебираем количество мин
#     rw, cl = (int(i) -1 for i in input().split())  # записываем строку и столбец одной мины при каждом проходе
#     a[rw][cl] = - 1  # записываем минус по координатам
# for i in range(rows):  # поиск мин вокруг # перебираем строки
#     for j in range(columns):  # перебираем столбцы
#         if a[i][j] == 0:  # ячейка без мины
#             for di in range(-1, 2):  # перебираем соседные строки -1 0 1
#                 for dj in range(-1, 2):  # перебираем соседние столбцы -1 0 1
#                     ai = i + di  # кординат по строке
#                     aj = j + dj  # координат по столбцу
#                     if 0 <= ai < rows and 0 <= aj < columns and a[ai][aj] == -1:  # проверка вхождения в диапазон
#                         # и мины по соседству
#                         a[i][j] += 1
# for i in range(rows):
#     for j in range(columns):
#         if a[i][j] == -1:
#             print('*', end='')
#         elif a[i][j] == 0:
#             print('.', end='')
#         else:
#             print(a[i][j], end='')
#     print()
#
# Задачи по материалам недели 6 out of 11 steps
#
#
# a = int(input())
# total = 0
# total += a
# quad = 0
# while total != 0:
#     quad += total ** 2
#     print(quad)
#     a = int(input())
#     total += a
#     quad += total ** 2
# print(quad)
#
#
# a = int(input())
# c = a ** 2
#
# while a != 0:
#     b = int(input())
#     a += b
#     c += b ** 2
# print(c)
# Задачи по материалам недели 7 out of 11 steps
#
# a = int(input())
# b = []
# s = len(b)
# i = 0
# j = 0
# while i < a:
#     i += 1
#     while i > j:
#         b.append(i)
#         j += 1
#         if len(b) == a:
#             break
#     j = 0
#     if len(b) == a:
#         break
# print(*b)
#
# Задачи по материалам недели 8 out of 11 steps
# n = int(7)  # считываем
# i = 1
# count = 0
#
# while count < n:  # условие на превышение переборов
#     for j in range(i):
#         if count < n:
#             print(i, end='')
#             count += 1
#         else:
#             break
#     i += 1
#
# Задачи по материалам недели 9 out of 11 steps
#
# lst = [int(i) for i in input().split()]
# b = []
# x = int(input())
# n = len(lst)
#
# if x in lst:
#     for i in range(n):
#         if lst[i] == x:
#             b.append(i)
#     print(*b)
# else:
#     print('Отсутствует')
#
#

#
#
# for i in range(3):
#     s = 0
#     for j in range(3):
#
#
# for i in range(len(a)):
#     s = 0
#     for j in range(len(a)):
#         if i == j:
#             if a[i][j] == a[0][0]:
#                 s = a[1][0] + a[2][0] + a[0][1] + a[0][2]
#                 print(s)
#             elif a[i][j] == a[1][1]:
#                 s = a[1][0] + a[0][1] + a[1][2] + a[2][1]
#                 print(s)
#             elif a[i][j] == a[2][2]:
#                 s = a[2][1] + a[1][2] + a[2][0] + a[0][2]
#                 print(s)
#         # elif i > j:
#         # elif i < j:
# a = [[int(i) for i in input().split()]]
# b = input()
# while b != 'end':
#     a.append([int(i) for i in b.split()])
#     b = input()
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i - 1][j] + a[i - len(a) + 1][j] + a[i][j - 1] + a[i][j - len(a[i]) + 1], end=' ')
#         print()
