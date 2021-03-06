"""
Магический шар 8
Описание проекта: магический шар 8 (шар судьбы) — шуточный способ предсказывать будущее. Программа должна просить пользователя задать некий вопрос, чтобы случайным образом на него ответить.

Составляющие проекта:
- Целые числа (тип int);
- Переменные;
- Ввод / вывод данных (функции input() и print());
- Условный оператор (if/elif/else);
- Цикл while;
- Бесконечный цикл;
- Операторы break, continue;
- Работа с модулем random для генерации случайных чисел.

https://stepik.org/lesson/349846/step/1?unit=333701
"""

import random

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
           'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
           'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
           'Перспективы не очень хорошие', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как тебя зововут?\n')
print(f'Привет, {name}!')


def is_magic_ball():
    while True:
        print(f'Задавайте Ваш вопрос, {name}!')
        input()
        print(random.choice(answers) + '.')
        n = input('Попробовать ещё раз? (д = да, н = нет): ')
        if n == 'д':
            is_magic_ball()
        elif n == 'н':
            print('Спасибо, что играли в со мной. Еще увидимся...')
            break


is_magic_ball()
