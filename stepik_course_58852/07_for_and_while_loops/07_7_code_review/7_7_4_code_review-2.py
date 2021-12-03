"""
Ревью кода-2 🌶️🌶️
На обработку поступает последовательность из 10 целых чисел. Известно, что вводимые числа по абсолютной величине
не превышают 10^6. Нужно написать программу, которая выводит на экран сумму всех отрицательных чисел последовательности
и максимальное отрицательное число в последовательности. Если отрицательных чисел нет, требуется вывести на экран
«NO». Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их ровно 5). Известно, что каждая ошибка затрагивает только одну строку и может
быть исправлена без изменения других строк.

Примечание 1. Число xx не превышает по абсолютной величине 10^6, если -10^6 ≤x ≤10^6.

Примечание 2. При необходимости вы можете добавить необходимые строки кода.

https://stepik.org/lesson/311433/step/4?auth=login&unit=2938611
"""
mx = -10**6 - 1
s = 0
for _ in range(10):
    x = int(input())
    if x < 0:
        s += x
        if 0 > x > mx:
            mx = x
if s < 0:
    print(s)
    print(mx)
else:
    print('NO')
