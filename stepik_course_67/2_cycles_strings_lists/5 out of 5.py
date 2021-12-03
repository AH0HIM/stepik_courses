"""
2.6 Задачи по материалам недели 5 out of 5:

Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали, выходящей из левого верхнего угла и
закрученной по часовой стрелке, как показано в примере (здесь n=5):

Sample Input:
5

Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

https://stepik.org/lesson/3369/step/11?unit=952
"""

# table = [[0, 0, 0],
#          [0, 0, 0],
#          [0, 0, 0]]
#
# h = table[0][0]
# table[0][0] = 1
#
# print(table)


n = 5                                       # num = int(input())
table = [[0] * n for i in range(n)]         # генерация таблицы с нулями
i, j = 0, 0                                 # столбец и строка

for element in range(1, n*n + 1):           # начинаю с 1, включительно 25
    table[i][j] = element                   #
    if i <= j + 1 and i + j < n - 1:        # заполняю правую сторону
        j += 1
    elif j >= i + 1:                        # опускаемся вниз сторону
        i += 1
    elif i >= j - 1 and i + j > n - 1:      # теперь наоборот влевую сторону
        j -= 1
    elif j <= i - 1:
        i -= 1                              # вверх

for i in table:                             # выводим заполненую таблицуы
    print(*i)


