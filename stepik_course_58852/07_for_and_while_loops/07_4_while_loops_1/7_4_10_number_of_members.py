"""
Количество членов
На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является одно из трех слов: «стоп», «хватит», «достаточно» (маленькими буквами, без кавычек). Напишите программу, которая выводит общее количество членов данной последовательности.

Формат входных данных
На вход программе подается последовательность слов, каждое слово на отдельной строке.

Формат выходных данных
Программа должна вывести общее количество членов данной последовательности.

https://stepik.org/lesson/265121/step/10?unit=246070
"""
text, count = input(), 0
while text not in ('стоп', 'хватит', 'достаточно'):
    count += 1
    text = input()
print(count)
