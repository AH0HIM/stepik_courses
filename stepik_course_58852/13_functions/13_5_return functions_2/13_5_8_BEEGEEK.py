"""
BEEGEEK
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.

Примечание. Следующий программный код:
print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))

должен выводить:
True
False
False
False

https://stepik.org/lesson/334150/step/8?unit=317559
"""


def is_valid_password(password):
    if len(password) == 3:
        return is_palindrome(password[0]) and is_prime(int(password[1])) and is_even_number(int(password[2]))

    return False


def is_palindrome(num):
    return num == num[:: -1]


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if not num % i:
            return False
    return True


def is_even_number(num):
    return num % 2 == 0


psw = input().split(':')

print(is_valid_password(psw))
