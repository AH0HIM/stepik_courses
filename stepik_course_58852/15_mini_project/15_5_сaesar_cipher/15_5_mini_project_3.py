"""
Шифр Цезаря
Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря. Она должна запрашивать у пользователя следующие данные:

направление: шифрование или дешифрование;
язык алфавита: русский или английский;
шаг сдвига (со сдвигом вправо).
Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).

Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.

Примечание 3. Сохраните регистр символов. Например, текст: "Умом Россию не понять" при сдвиге на одну позицию вправо будет преобразован в: "Фнпн Спттйя ож рпоауэ".

Составляющие проекта:
- Целые числа (тип int);
- Модульная арифметика;
- Переменные;
- Ввод / вывод данных (функции input() и print());
- Условный оператор (if/elif/else);
- Цикл for/while;
- Строковые методы.

https://stepik.org/lesson/352860/step/4?unit=336821
"""
txt = input('Введите текст:\n')
direction = input('Направление: шифрование или дешифрование?\n')
language = input('Язык алфавита: русский или английский?\n')
if language == 'русский':
    lang = [chr(i) for i in range(1072, 1104)]
if language == 'английский':
    lang = [chr(i) for i in range(97, 123)]
step = int(input('Шаг сдвига (со сдвигом вправо)?\n'))


def encryption(lang, step, txt):
    result = ''
    for i in txt:
        if i in lang:
            result += lang[(lang.index(i) + step) % len(lang)]
        elif i.lower() in lang:
            result += lang[(lang.index(i.lower()) + step) % len(lang)].upper()
        else:
            result += i

    return result


def decryption(lang, step, txt):
    result = ''
    for i in txt:
        if i in lang:
            result += lang[(lang.index(i) - step) % len(lang)]
        elif i.lower() in lang:
            result += lang[(lang.index(i.lower()) - step) % len(lang)].upper()
        else:
            result += i

    return result


def caesar():
    if direction == 'шифрование':
        return encryption(lang, step, txt)
    if direction == 'дешифрование':
        return decryption(lang, step, txt)


print(caesar())
