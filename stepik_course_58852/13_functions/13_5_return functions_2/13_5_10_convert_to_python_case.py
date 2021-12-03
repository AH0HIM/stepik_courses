"""
Змеиный регистр
Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

Примечание 1. Почитать подробнее о стилях именования можно тут.

Примечание 2. Следующий программный код:
print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))

должен выводить:
this_is_camel_cased
is_prime_number

https://stepik.org/lesson/334150/step/10?unit=317559
"""


def is_convert_to_python_case(text):
    result = text[0].lower()
    for i in range(1, len(text)):
        if text[i].isupper():
            result += '_'
            result += text[i].lower()
        else:
            result += text[i]
    return result


txt = input()

print(is_convert_to_python_case(txt))