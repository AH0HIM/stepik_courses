"""
Правильная скобочная последовательность 🌶️
Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую из символов ( и ) и возвращает значение True если поступившая на вход строка является правильной скобочной последовательностью и False в противном случае.

Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только из символов ( и ), где каждой открывающей скобке найдется парная закрывающая скобка.

Примечание 2. Следующий программный код:
print(is_correct_bracket('()(()())'))
print(is_correct_bracket(')(())('))

должен выводить:
True
False

https://stepik.org/lesson/334150/step/9?unit=317559
"""


def is_correct_bracket(text):
    count = 0
    for i in range(len(text)):
        if text[i] == '(':
            count += 1
        if text[i] == ')':
            count -= 1
        if count == -1:
            return False
    if count == 0:
        return True
    else:
        return False


txt = '())(()'

print(is_correct_bracket(txt))
