# # 1. Операторы. Переменные. Типы данных.
# #Условия.12 Задачи по материалам недели 1_operators_variables_data-types_conditions out of 7:
#
# a = int(input())
# b = int(input())
# c = int(input())
# s = (a + b + c)/2
# print((s*(s-a)*(s-b)*(s-c))**0.5)
#
# # 1_operators_variables_data-types_conditions.12 Задачи по материалам недели 2_cycles_strings_lists out of 7:
#
# sum = int(input())
#
# if -15 < sum <= 12 or 14 < sum < 17 or sum >= 19:
#     print('True')
# else:
#     print('False')
#
# # Задачи по материалам недели 3 out of 7 steps
#
# a = float(input())
# b = float(input())
# c = str(input())
#
# if c == 'mod' or c == 'div' or c == '/' and b == 0:
#     print('Деление на 0!')
# elif c == 'mod':
#     print(a % b)
# elif c == 'pow':
#     print(a ** b)
# elif c == 'div':
#     print(a // b)
# elif c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)
# elif c == '/':
#     print(a / b)
# elif c == '*':
#     print(a * b)
#
# # Задачи по материалам недели 4 out of 7 steps
#
# str = str(input())
#
# if str == 'треугольник':
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     s = (a + b + c) / 2
#     print(float((s * (s - a) * (s - b) * (s - c)) ** 0.5))
# elif str == 'прямоугольник':
#     a = int(input())
#     b = int(input())
#     print(float(a * b))
# elif str == 'круг':
#     r = int(input())
#     print(float(3.14 * (r ** 2)))
#
# # 1_operators_variables_data-types_conditions.12 Задачи по материалам недели 5 out of 7:
#
# a, b, c = int(input()), int(input()), int(input())
#
# if a < b:
#     a, b = b, a
# if a < c:
#     a, c = c, a
# if b > c:
#     b, c = c, b
#
# print(a)
# print(b)
# print(c)
#
#
# # 1. Operators. Variables. Data types. Conditions1. Условия.12 Задачи по материалам недели 6 out of 7:
#
# n = int(input())
#
# if n % 10 == 1 and n % 100 != 11:
#     print(n, 'программист')
# elif 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
#     print(n, 'программиста')
# else:
#     print(n, 'программистов')
#
# # 1_operators_variables_data-types_conditions.12 Задачи по материалам недели 7 out of 7:
#
# n = int(input())
#
# num1 = n // 100000
# num2 = (n // 10000) % 10
# num3 = (n // 1000) % 10
# num4 = (n % 1000) // 100
# num5 = (n % 100) // 10
# num6 = n % 10
#
# if num1 + num2 + num3 == num4 + num5 + num6:
#     print('Счастливый')
# else:
#     print('Обычный')
#
# a, b, c, d, e, f = input()
#
# if int(a) + int(b) + int(c) == int(d) + int(e) + int(f):
#     print('Счастливый')
# else:
#     print('Обычный')
