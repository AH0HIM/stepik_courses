"""
Генератор безопасных паролей
Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.

Составляющие проекта:
- Целые числа (тип int);
- Переменные;
- Ввод / вывод данных (функции input() и print());
- Условный оператор (if/elif/else);
- Цикл for;
- Написание пользовательских функций;
- Работа с модулем random для генерации случайных чисел.

https://stepik.org/lesson/349848/step/1?unit=333703
"""
import random


def is_generator_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''

quantity = int(input('Укажите количество паролей для генерации: '))
length = int(input('Задайте длину одного пароля: '))


if input('Включать ли цифры "0123456789"? (д = да, н = нет): ') == 'д':
    chars += digits
if input('Включать ли строчные буквы "abcdefghijklmnopqrstuvwxyz"? (д = да, н = нет): ') == 'д':
    chars += lowercase_letters
if input('Включать ли прописные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"? (д = да, н = нет): ') == 'д':
    chars += uppercase_letters
if input('Исключать ли неоднозначные символы "!#$%&*+-=?@^_"? (д = да, н = нет): ') == 'д':
    chars += punctuation
if input('Исключить символы "il1Lo0O"? (д = да, н = нет): ') == 'д':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')


for _ in range(quantity):
    print(is_generator_password(length, chars))


