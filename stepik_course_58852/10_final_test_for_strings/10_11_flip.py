"""
Переворот
На вход программе подается строка текста в которой буква «h» встречается как минимум два раза. Напишите программу,
которая возвращает исходную строку и переворачивает последовательность символов, заключенную между первым и последним
вхождением буквы «h».

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

https://stepik.org/lesson/313233/step/11?unit=295750
"""

s = input()

a = int(s.find('h'))
b = int(s.rfind('h'))

print(s[:a] + s[b:a: - 1] + s[b:])
