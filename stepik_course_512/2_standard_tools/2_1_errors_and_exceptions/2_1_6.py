"""
Вашей программе будет доступна функция foo, которая может бросать исключения.

Вам необходимо написать код, который запускает эту функцию, затем ловит исключения ArithmeticError, AssertionError, ZeroDivisionError и выводит имя пойманного исключения.

Пример решения, которое вы должны отправить на проверку.

https://stepik.org/lesson/24463/step/6?thread=solutions&unit=6771
"""
try:
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError")
except AssertionError:
    print("AssertionError")
except ArithmeticError:
    print("ArithmeticError")