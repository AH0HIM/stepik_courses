"""
Хороший оттенок
На вход программе подается строка текста. Напишите программу, которая определяет является ли оттенок текста хорошим или
нет. Текст имеет хороший оттенок, если содержит подстроку «хорош» во всевозможных регистрах.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести «YES» если текст имеет хороший оттенок и «NO» в противном случае.

Примечание. Текст содержащий хорош, ХОРОШ, Хорош, хОРОШ и т.д. имеет хороший оттенок.

https://stepik.org/lesson/296416/step/10?unit=278136
"""
if 'хорош' in input().lower():
    print('YES')
else:
    print('NO')

