"""
Реализуйте программу, которая принимает последовательность чисел и выводит их сумму.

Вашей программе на вход подается последовательность строк.
Первая строка содержит число n (1 ≤ n ≤ 100).
В следующих n строках содержится по одному целому числу.

Выведите одно число – сумму данных n чисел.

Примечание:
Чтобы считать одно число из стандартного потока ввода, можно использовать, например, следующий код
n = int(input())

https://stepik.org/lesson/24456/step/9?unit=6762
"""
numbers = int(input())           # первая строка
sum = 0                          # сумма данных n чисел

for i in range(numbers):         # цикл в диапазоне первой числа
    sum += int(input())          # прибавление следующих n строк
print(sum)
