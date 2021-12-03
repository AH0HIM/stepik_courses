"""
Дополните приведенный код, так чтобы элемент списка имеющий значение Green заменился на значение Зеленый, а элемент
Violet на Фиолетовый. Далее необходимо вывести полученный список.

https://stepik.org/lesson/296419/step/7?unit=278139
"""

rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

rainbow[3], rainbow[-1] = 'Зеленый', 'Фиолетовый'

print(rainbow)
