"""
В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней,
равное days.

Примечание:
Для решения этой задачи используйте стандартный модуль datetime.
Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате.

https://stepik.org/lesson/24466/step/5?unit=6773
"""

import datetime

date = datetime.datetime.strptime(input(), '%Y %m %d')
date += datetime.timedelta(days=int(input()))

print(f'{date.year} {date.month} {date.day}')
