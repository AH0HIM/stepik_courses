from random import *

print('Добро пожаловать в числовую угадайку!')
num = 0


def is_random_num():
    return num == randint(1, int(input('Укажите граниченое значение: ')))


def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100


def is_again_game():
    n = input('Попробовать ещё раз? (д = да, н = нет): ')
    if n == 'д':
        is_random_num()
        print('Игра началась!')
        return is_valid_num()
    elif n == 'н':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    else:
        print('Введено некорректное значение!')
        return is_again_game()


def is_valid_num():
    count = 0
    is_random_num()
    while True:
        n = input('Введите число: ')
        if not is_valid(n):
            print('А может быть все-таки введем целое число от 1 до 100?')
        else:
            n = int(n)
            if n == num:
                count += 1
                print('Вы угадали, поздравляем!')
                print('Число попыток:', count)
                is_again_game()
            elif n < num:
                print('Ваше число меньше загаданного, попробуйте еще разок.')
                count += 1
            elif n > num:
                print('Ваше число больше загаданного, попробуйте еще разок.')
                count += 1


is_valid_num()
