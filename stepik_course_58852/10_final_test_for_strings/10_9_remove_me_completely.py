"""
Удали меня полностью
На вход программе подается строка текста. Напишите программу, которая удаляет все вхождения символа «@».

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

https://stepik.org/lesson/313233/step/9?unit=295750
"""

s = input()

print(s.replace('@', ''))