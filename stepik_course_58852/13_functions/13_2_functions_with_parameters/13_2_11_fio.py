"""
ФИО
Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:

name – имя человека;
surname – фамилия человека;
patronymic – отчество человека;
а затем выводит на печать ФИО человека.

Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь

https://stepik.org/lesson/333525/step/9?unit=316953
"""


def print_fio(name, surname, patronymic):
    [print(i[0].upper(), end='') for i in [surname, name, patronymic]]


name, surname, patronymic = input(), input(), input(),

print_fio(name, surname, patronymic)
