"""
Перевод чисел из любой системы счисления в десятичную

https://stepik.org/lesson/349851/step/2?unit=333706
"""


def calculator(b, n):
    result = 0
    for i in range(len(b)):
        if b[i] == 'A':
            result += int(10) * int(n) ** ((len(b) - 1) - i)
        if b[i] == 'B':
            result += int(11) * int(n) ** ((len(b) - 1) - i)
        if b[i] == 'C':
            result += int(12) * int(n) ** ((len(b) - 1) - i)
        if b[i] == 'D':
            result += int(13) * int(n) ** ((len(b) - 1) - i)
        if b[i] == 'E':
            result += int(14) * int(n) ** ((len(b) - 1) - i)
        if b[i] == 'F':
            result += int(15) * int(n) ** ((len(b) - 1) - i)
        if b[i].isdigit():
            result += int(b[i]) * int(n) ** ((len(b) - 1) - i)

    print(result)


base = '1000'  # input('Введите основание степени: \n')
number = 10  # input('Введите показатель степени: \n')

calculator(base, number)
