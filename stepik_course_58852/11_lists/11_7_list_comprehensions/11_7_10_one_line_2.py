"""
В одну строку 2
На вход программе подается строка текста. Напишите программу, использующую списочное выражение, которая выводит все цифровые символы данной строки.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Программу можно написать в одну строку кода.

https://stepik.org/lesson/326725/step/10?unit=310010
"""

[print(*i, end='') for i in input() if i.isdigit()]
