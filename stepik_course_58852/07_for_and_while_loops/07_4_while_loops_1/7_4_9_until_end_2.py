"""
До КОНЦА 2
На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности
является слово «КОНЕЦ» или «конец» (большими или маленькими буквами, без кавычек). Напишите программу, которая выводит
члены данной последовательности.

Формат входных данных
На вход программе подается последовательность слов, каждое слово на отдельной строке.

Формат выходных данных
Программа должна вывести члены данной последовательности.

https://stepik.org/lesson/265121/step/9?auth=login&unit=246070
"""
text = input()

while text != 'КОНЕЦ' and text != 'конец':
    print(text)
    text = input()
