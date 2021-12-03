"""
Good password 🌶️
Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является надежным и False в противном случае.

Пароль является надежным если:

его длина не менее 88 символов;
он содержит как минимум одну заглавную букву (верхний регистр);
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.
 Примечание. Следующий программный код:

print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))
должен выводить:

True
False


https://stepik.org/lesson/334150/step/5?unit=317559
"""


def is_good_password(password):
    flag_lower = False
    flag_upper = False
    flag_digit = False
    if len(password) >= 8:
        for i in password:
            if i.islower():
                flag_lower = True
            if i.isupper():
                flag_upper = True
            if i.isdigit():
                flag_digit = True
    else:
        return False
    if flag_lower and flag_upper and flag_digit:
        return True
    else:
        return False


txt = input()

print(is_good_password(txt))
