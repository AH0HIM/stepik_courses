# Задача 1. Напишите программу, которая определяет, является ли заданное натуральное число трёхзначным.
#
# num = int(input())
# if 100 <= num <= 999:
#     print('Число является трёхзначным')
# else:
#     print('Число не является трёхзначным')
#
# Задача 2. Напишите программу, которая проверяет, что все три цифры натурального трёхзначного числа различны.
#
# num = int(input())
# d3 = num % 10
# d2 = num % 100 // 10
# d1 = num // 100
# if d3 != d2 and d3 != d1 and d2 != d1:
#     print('Цифры различны')
# else:
#     print('Цифры не различны')
#
#
# Задача 3. Напишите программу, которая по координатам точки, не лежащей на осях координат,
# определяет номер координатной четверти, в которой она находится.
#
# x = int(input())
# y = int(input())
#
# if x > 0 and y > 0:
#     print('1 четверть')
# if x < 0 and y > 0:
#     print('2 четверть')
# if x < 0 and y < 0:
#     print('3 четверть')
# if x > 0 and y < 0:
#     print('4 четверть')
# num = int(input())
# if -2 >= num > -30 or 7 < num <= 25:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')
#
# num = int(input())
# if (1000 <= num <= 9999) and ((num % 7) == 0 or (num % 17) == 0):
#     print('YES')
# else:
#     print('NO')
#
#
# a, b, c = int(input()), int(input()), int(input())
# if a + b > c and b + c > a and a + c > b:
#     print('YES')
# else:
#     print('NO')
#
# year = int(input())
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('YES')
# else:
#     print('NO')
#
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
#
# if x1 == x2 or y1 == y2:
#     print('YES')
# else:
#     print('NO')
#
#
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if (x2 - 1 <= x1 <= x2 + 1) and (y2 - 1 <= y1 <= y2 + 1):
#     print('YES')
# else:
#     print('NO')
# Задача 1. Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел:
# 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).
#
#
# a, b, c = int(input()), int(input()), int(input())
# if a == b:
#     if b == c:
#         print(3)
#     else:
#         print(3)
# else:
#     if a == c:
#         print(2)
#     else:
#         if b == c:
#             print(2)
#         else:
#             print(0)
#
# a, b, c = int(input()), int(input()), int(input())
#
# if a == b == c:
#     print(3)
# elif a == b != c:
#     print(2)
# elif a != b == c:
#     print(2)
# elif a == c != b:
#     print(2)
# else:
#     print(0)
#
# a, b, c = int(input()), int(input()), int(input())
#
# if a == b == c:
#     print(3)
# elif a != b == c or a == b != c or a == c != b:
#     print(2)
# else:
#     print(0)
#
# zum = int(input())
# flash = int(input())
#
# if zum > flash:
#     print('NO')
# elif flash > zum:
#     print('YES')
# else:
#     print("Don't know")
#
# a, b, c = int(input()), int(input()), int(input())
#
# if a == b == c and c == a:
#     print('Равносторонний')
# elif a == b != c or b == c != a or c == a != b:
#     print('Равнобедренный')
# else:
#     print('Разносторонний')
#
# a, b, c = int(input()), int(input()), int(input())
#
# if b < a < c or b > a > c:
#     print(a)
# elif a < b < c or a > b > c:
#     print(b)
# else:
#     print(c)
#
# month = int(input())
#
# if month == 2:
#     print('28')
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     print('30')
# else:
#     print('31')
#
# a = int(input())
#
# if a < 60:
#     print('Легкий вес')
# elif a < 64:
#     print('Первый полусредний вес')
# elif a < 69:
#     print('Полусредний вес')
#
# num1, num2, string = int(input()), int(input()), str(input())
#
# if string == '+':
#     print(num1 + num2)
# elif string == '-':
#     print(num1 - num2)
# elif string == '*':
#     print(num1 * num2)
# elif string == '/':
#     if num2 != 0:
#         print(num1 / num2)
#     else:
#         print('На ноль делить нельзя!')
# else:
#     print('Неверная операция')
#
# c1, c2 = str(input()), str(input())
# red = 'красный'
# blue = 'синий'
# yellow = 'желтый'
#
# if c1 == red:
#     if c1 == red and c2 == red:
#         print('красный')
#     else:
#         if c2 == blue:
#             print('фиолетовый')
#         else:
#             if c2 == yellow:
#                 print('оранжевый')
#             else:
#                 print('ошибка цвета')
# elif c1 == blue:
#     if c1 == blue and c2 == blue:
#         print('синий')
#     else:
#         if c2 == red:
#             print('фиолетовый')
#         else:
#             if c2 == yellow:
#                 print('зеленый')
#             else:
#                 print('ошибка цвета')
# elif c1 == yellow:
#     if c1 == yellow and c2 == yellow:
#         print('желтый')
#     else:
#         if c2 == blue:
#             print('зеленый')
#         else:
#             if c2 == red:
#                 print('оранжевый')
#             else:
#                 print('ошибка цвета')
# else:
#     print('ошибка цвета')
#
# c1, c2 = str(input()), str(input())
# red = 'красный'
# blue = 'синий'
# yellow = 'желтый'
#
# if (c1 == red and c2 == blue) or (c1 == blue and c2 == red):
#     print('фиолетовый')
# elif (c1 == blue and c2 == yellow) or (c1 == yellow and c2 == blue):
#     print('зеленый')
# elif (c1 == yellow and c2 == red) or (c1 == red and c2 == yellow):
#     print('оранжевый')
# elif c1 == blue and c2 == blue:
#     print('синий')
# elif c1 == red and c2 == red:
#     print('красный')
# elif c1 == yellow and c2 == yellow:
#     print('желтый')
# else:
#     print('ошибка цвета')
#
# number = int(input())
#
# if number == 0:
#     print('зеленый')
# elif 1 <= number <= 10:
#     if number % 2 == 0:
#         print('черный')
#     else:
#         print('красный')
# elif 11 <= number <= 18:
#     if number % 2 == 0:
#         print('красный')
#     else:
#         print('черный')
# elif 19 <= number <= 28:
#     if number % 2 == 0:
#         print('черный')
#     else:
#         print('красный')
# elif 29 <= number <= 36:
#     if number % 2 == 0:
#         print('красный')
#     else:
#         print('черный')
# else:
#     print('ошибка ввода')
#
#
# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
#
# if b1 < a2 or b2 < a1:
#     print('пустое множество')
# elif (a2 > a1 and b2 < b1) and (a1 != b2):
#     print(a2, b2)
# elif (a2 > a1 and b2 > b1) and (b1 != a2):
#     print(a2, b1)
# elif (a2 < a1 and b2 < b1) and (b2 != a1):
#     print(a1, b2)
# elif (a2 < a1 and b2 > b1) and (a1 != a2 and b1 != b2):
#     print(a1, b1)
# elif (a1 < b1 and a2 < b2) and (b1 == a2):
#     print(b1)
# elif (a1 < b1 and a2 < b2) and (b2 == a1):
#     print(a1)
# elif (a1 < b1 and a2 < b2) and (a2 == a1 and b2 == b1):
#     print(a1, b2)
# elif (a1 < b1 and a2 < b2) and (a2 == a1 and b2 != b1) and (b1 < b2):
#     print(a1, b1)
# elif (a1 < b1 and a2 < b2) and (a2 != a1 and b2 == b1) and (a2 < a1):
#     print(a1, b2)
# elif (a1 < b1 and a2 < b2) and (a2 != a1 and b2 == b1) and (a1 < a2):
#     print(a2, b2)
# elif (a1 < b1 and a2 < b2) and (a2 == a1 and b2 != b1) and (b2 < b1):
#     print(a1, b2)
"""
Решение задач
Задача 1. Напишите функцию, которая возвращает длину гипотенузы прямоугольного треугольника по известным
значениям его катетов.

"""
