"""
Стоимость строки

Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ (в том числе пробел) стоит 6060 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.

Формат входных данных
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести стоимость строки.

https://stepik.org/lesson/415553/step/4?unit=405082
"""

text = input()
print(((len(text) * 60) // 100), 'р.', (len(text) * 60) % 100, 'коп.')